"""Local development interface. Start with run_application.py after setup."""
import json
from pathlib import Path

import streamlit as st

from application_engine import ApplicationEngine, ConnectionSettings, QueryStageError
from application_view import MODE_LABELS, add_history, graph_html
from schemas import AnswerResponse, QueryRequest

REPO = Path(__file__).resolve().parent


def disconnect():
    if 'engine' in st.session_state:
        st.session_state.pop('engine').close()
    st.session_state.pop('neo4j_password', None)


def render_result(record):
    answer = AnswerResponse.model_validate(record['answer'])
    st.subheader(record['request']['question'])
    st.caption(MODE_LABELS[record['request']['mode']]+' · '+
        answer.generation_timestamp.strftime('%Y-%m-%d %H:%M UTC')+
        f' · {answer.execution_time_ms/1000:.2f} seconds')
    if answer.abstained:
        st.info('Some or all requested information was unavailable in the retrieved evidence.')
    if answer.claims:
        for claim in answer.claims:
            # Plain text prevents source/model strings becoming executable HTML or links.
            st.text(claim.text+' ['+', '.join(claim.citations)+']')
    else:
        st.text(answer.answer)
    st.caption('Citations link to supplied evidence. They do not establish that a claim is correct.')
    source_tab, graph_tab, details_tab = st.tabs(['Sources', 'Query graph', 'Run details'])
    with source_tab:
        for passage in answer.evidence.passages:
            info = record['sources'].get(passage.doc_id, {})
            label = 'CISA advisory' if passage.source_kind == 'cisa' else 'ATT&CK reference guidance'
            with st.expander(passage.citation_id+' · '+label+' · '+passage.doc_id):
                st.text(info.get('title', passage.doc_id))
                st.caption('Source date: '+(info.get('publication_date') or 'Not recorded')+
                    f' · Source span {passage.start}:{passage.end}')
                st.link_button('Open source', str(passage.source_url))
                st.text(passage.text)
    with graph_tab:
        if answer.evidence.paths:
            st.caption('Accepted directed paths returned for this question. This is the query-time graph snapshot; it is not refreshed automatically.')
            st.html(graph_html(answer, record['entities']), unsafe_allow_javascript=True)
        else:
            st.info('This answer has no returned graph paths.')
    with details_tab:
        st.text('Human source review pending · Model: '+record['model_digest'])
        st.json(record['retrieval'])
        st.text('Saved results: '+record['folder'])
        st.download_button('Download this result', json.dumps(record, indent=2),
            file_name='threatweave-answer.json', mime='application/json', key='download-'+record['folder'])


def main():
    st.set_page_config(page_title='ThreatWeave', page_icon='🕸️', layout='wide')
    st.title('ThreatWeave')
    st.caption('Explore CISA observations and ATT&CK guidance with cited answers.')
    st.info('Development evidence only. Broader corpus processing and final evaluation are unfinished.')
    config = json.loads((REPO/'config.json').read_text(encoding='utf-8'))
    state = st.session_state
    if 'history' not in state:
        state['history'] = []
    with st.sidebar:
        st.header('Ask with')
        mode = st.selectbox('Retrieval mode', list(MODE_LABELS), format_func=MODE_LABELS.get)
        st.caption({'hybrid': 'Text, source-supported graph paths and graph neighbors.',
            'text_only': 'Text search only. Neo4j is not needed.',
            'graph_only': 'Source-supported graph paths only.',
            'hybrid_no_node2vec': 'Text and source-supported paths, without graph neighbors.'}[mode])
        with st.expander('Connection settings', expanded='engine' not in state):
            uri = st.text_input('Neo4j URI', 'bolt://localhost:7687')
            username = st.text_input('Username', 'neo4j')
            database = st.text_input('Database', 'neo4j')
            password = st.text_input('Neo4j password', type='password', key='neo4j_password')
            st.caption('Keep Ollama running. Graph modes also need Neo4j. Connection changes require a reconnect.')
            st.button('Disconnect / reconnect', on_click=disconnect)
        if st.button('Clear visible history'):
            state['history'] = []
            st.rerun()
        st.caption('History stays in this browser session. Each question uses only its own retrieved evidence. Saved run records remain on disk.')
    with st.form('ask', clear_on_submit=False):
        question = st.text_area('Your question', placeholder='According to CISA, how do Rhysida actors use valid accounts?', max_chars=2000)
        submitted = st.form_submit_button('Ask ThreatWeave', type='primary')
    if submitted:
        try:
            request = QueryRequest(question=question.strip(), mode=mode, corpus_version=config['corpus_version'])
            with st.spinner('Checking sources and preparing your answer. The first query in a mode may take longer.'):
                if 'engine' not in state:
                    state['engine'] = ApplicationEngine(REPO, ConnectionSettings(uri, username, database, password))
                result = state['engine'].execute(request)
                state['history'] = add_history(state['history'], result)
        except QueryStageError as error:
            st.error(str(error))
            st.caption('Failed stage: '+error.stage)
            if error.folder:
                st.caption('A failure receipt was saved in '+error.folder)
        except ValueError:
            st.error('Enter a question of at least three characters and check the connection settings. If source preparation changed, reconnect.')
        except Exception:
            st.error('The application could not complete this request. Check local setup and reconnect.')
    if state['history']:
        labels = {i: f'{i+1}. {MODE_LABELS[r["request"]["mode"]]} · {r["request"]["question"][:75]}'
                  for i, r in enumerate(state['history'])}
        selected = st.selectbox('Answer history', list(labels), index=len(labels)-1, format_func=labels.get)
        render_result(state['history'][selected])
    else:
        st.caption('Ask a question to see its answer, exact source passages and returned graph paths.')


if __name__ == '__main__':
    main()
