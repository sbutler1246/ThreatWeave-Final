"""Replay real preserved application results through the production result renderer.

This demonstration never constructs a model, retriever, or database adapter.
"""
import json
from pathlib import Path

import streamlit as st

from streamlit_app import render_result

ROOT = Path(__file__).resolve().parent
RECORDS = {
    'Graph only, saved October 15': 'work/application_qa/20261015T074134Z-a878f56c/display.json',
    'Full hybrid, saved October 15': 'work/application_qa/20261015T165813Z-950f9f1f/display.json',
}


def main():
    st.set_page_config(page_title='ThreatWeave saved-run demo', page_icon='🕸️', layout='wide')
    st.title('ThreatWeave')
    st.caption('CISA observations and ATT&CK guidance with cited answers')
    st.info('Saved-run replay. These are real preserved application outputs. This demo makes no new model or database calls.')
    with st.sidebar:
        st.header('Saved application runs')
        selected = st.selectbox('Choose a saved run', list(RECORDS))
        st.caption('The original application renderer displays each preserved answer, evidence pack, graph, and export.')
        st.caption('Graph only uses source-supported paths. Full hybrid combines text, graph paths, and graph neighbors.')
        st.markdown('**Demo scope**')
        st.write('Inspect source citations, select graph nodes, pan or zoom the graph, switch saved runs, and download a structured run export.')
        st.caption('Saved answers can omit facts or contain errors. Citations identify the evidence supplied to generation.')
        st.caption('Original run notices describe the October 15 development checkpoint. Graph layout fields may appear in an export.')
    record = json.loads((ROOT / RECORDS[selected]).read_text(encoding='utf-8'))
    render_result(record)


if __name__ == '__main__':
    main()
