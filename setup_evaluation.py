"""Operator-only installation of the hash-locked, separate scoring environment.

Does not load embeddings, call Ollama/Neo4j, or score final answers.
"""
import argparse
import hashlib
import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def setup(repo, *, preview=False):
    repo = Path(repo).resolve()
    verification = json.loads((repo/'evaluation/dependency_verification.json').read_text(encoding='utf-8'))
    lock = repo/'evaluation/requirements.lock.txt'
    if hashlib.sha256(lock.read_bytes()).hexdigest() != verification['lock_sha256']:
        raise ValueError('Evaluator dependency lock hash changed.')
    target = repo/'.venv-eval'; python = target/'Scripts/python.exe'
    if target.is_symlink() or target.is_junction() or target.resolve().parent != repo:
        raise ValueError('Evaluator environment must stay inside this workspace.')
    if preview:
        print('PREVIEW PASSED: separate evaluator environment:',target)
        print('Locked package count:',verification['locked_package_count'])
        print('No installation, model loading, or service calls were performed.')
        return 0
    if sys.version_info[:2] != (3,12) or sys.platform != 'win32' or platform.machine().lower() not in {'amd64','x86_64'}:
        raise ValueError('The frozen evaluator lock requires Windows x64 Python 3.12.')
    if target.exists() and not (target/'pyvenv.cfg').is_file():
        raise ValueError('Existing evaluator path is not a virtual environment; it will not be overwritten.')
    if target.exists() and 'include-system-site-packages = false' not in (target/'pyvenv.cfg').read_text(encoding='utf-8').lower():
        raise ValueError('The separate evaluator environment must exclude system/application packages.')
    folder = repo/'work/evaluation_setup_runs'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    folder.mkdir(parents=True)
    receipt = {'status':'started', 'environment':str(target), 'lock_sha256':verification['lock_sha256'],
               'model_calls':0, 'scores_computed':False}
    def save():
        (folder/'setup_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    def command(args, name):
        print('Scoring setup:',name,flush=True)
        with (folder/(name+'.log')).open('w',encoding='utf-8') as log:
            result = subprocess.run(args,cwd=repo,stdout=log,stderr=subprocess.STDOUT)
        if result.returncode:
            raise RuntimeError(f'{name} failed; see {folder/(name+".log")}')
    save()
    try:
        if not python.is_file():
            command([sys.executable,'-m','venv',str(target)],'create_environment')
        interpreter_check = ('import sys,platform; from pathlib import Path; '
                             'assert sys.version_info[:2] == (3,12); '
                             'assert platform.machine().lower() in {"amd64","x86_64"}; '
                             f'assert Path(sys.prefix).resolve() == Path({str(target)!r}).resolve(); '
                             'print("Separate Windows x64 Python 3.12 evaluator verified.")')
        command([str(python),'-c',interpreter_check],'interpreter_check')
        command([str(python),'-m','pip','install','--require-hashes','-r',str(lock)],'install_locked_packages')
        command([str(python),'-m','pip','check'],'dependency_check')
        # Import checks only. Constructors and live evaluators are not executed.
        probe = ('from evaluation.run_ragas import require_pinned_versions; require_pinned_versions(); '
                 'from ragas import EvaluationDataset,evaluate; '
                 'from ragas.metrics import Faithfulness,ResponseRelevancy,LLMContextRecall; '
                 'from langchain_ollama import ChatOllama; '
                 'from langchain_huggingface import HuggingFaceEmbeddings; '
                 'from ragas.llms import LangchainLLMWrapper; '
                 'from ragas.embeddings import LangchainEmbeddingsWrapper; '
                 'print("Pinned evaluator imports passed; no model calls.")')
        os.environ['RAGAS_DO_NOT_TRACK'] = 'true'
        os.environ['HF_HUB_OFFLINE'] = '1'
        os.environ['TRANSFORMERS_OFFLINE'] = '1'
        command([str(python),'-c',probe],'adapter_import_check')
        command([str(python),'-m','pip','freeze'],'installed_environment')
        receipt['status'] = 'ready_for_live_evaluator_integration'
        print('EVALUATOR SETUP READY: locked dependencies and adapter imports passed.',flush=True)
    except Exception as error:
        receipt.update(status='failed',error=str(error))
        print('EVALUATOR SETUP FAILED:',error,flush=True)
    finally:
        receipt['finished_at'] = datetime.now(timezone.utc).isoformat();save()
        print('Saved setup records:',folder,flush=True)
    return 0 if receipt['status']=='ready_for_live_evaluator_integration' else 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preview',action='store_true')
    args = parser.parse_args()
    raise SystemExit(setup(Path(__file__).resolve().parent,preview=args.preview))
