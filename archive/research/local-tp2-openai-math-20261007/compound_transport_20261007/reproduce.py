"""Replay both exact methods in a clean temporary directory and compare all arrays.
Run `python3 reproduce.py` in the VS Code integrated terminal on a Mac.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,platform,shutil,subprocess,sys,tempfile,time
ROOT=Path(__file__).resolve().parent
SOURCES=('author.py','verifier.py','test_contracts.py','reproduce.py','README.md','THEOREM.md')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())
    for name in SOURCES:
        if sha(ROOT/name)!=manifest['sha256'][name]:raise ValueError('source hash mismatch: '+name)
    runs=[];comparisons=[]
    with tempfile.TemporaryDirectory(prefix='tp2-compound-') as tmp:
        work=Path(tmp)
        for name in SOURCES:shutil.copy2(ROOT/name,work/name)
        for command in [('author.py',),('verifier.py',),('-m','unittest','test_contracts','-v')]:
            start=time.monotonic()
            proc=subprocess.run([sys.executable,*command],cwd=work,capture_output=True,text=True,timeout=45)
            runs.append(dict(command=['python3',*command],exit_code=proc.returncode,
                             elapsed_seconds=round(time.monotonic()-start,4),
                             stdout=proc.stdout,stderr=proc.stderr))
            if proc.returncode:
                print(proc.stdout,proc.stderr,file=sys.stderr);raise RuntimeError('replay failed')
        out=ROOT/'certificates';out.mkdir(exist_ok=True)
        for label in ['root_R','LRL_R']:
            ap=work/'generated'/('author_'+label+'.json');vp=work/'generated'/('verifier_'+label+'.json')
            aa=json.loads(ap.read_text());vv=json.loads(vp.read_text())
            if aa['arrays']!=vv['arrays']:raise ValueError('full coefficient array mismatch: '+label)
            for key,value in vv['summary'].items():
                if aa['summary'][key]!=value:raise ValueError('summary mismatch: '+key)
            for src in [ap,vp]:shutil.copy2(src,out/src.name)
            comparisons.append(aa['summary'])
    for name in SOURCES:
        if sha(ROOT/name)!=manifest['sha256'][name]:raise ValueError('source changed: '+name)
    report=dict(status='PASS',completed_utc=datetime.now(timezone.utc).isoformat(),
                base_commit=manifest['base_commit'],python=platform.python_version(),
                exact_arithmetic='integers and fractions.Fraction; no floating-point proof decisions',
                runs=runs,comparisons=comparisons,
                certificate_entries_matched=sum(c['coefficient_count'] for c in comparisons),
                contract_tests=7,source_hashes_unchanged=True,
                scope='General conditional transport lemmas; alternative certificates for already-covered rays; full-tree OPEN',
                independence='Same-model separate algorithms, not blind/external/formal verification')
    (ROOT/'RUN_REPORT.json').write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['status','certificate_entries_matched','contract_tests','scope']},ensure_ascii=False))
    return 0
if __name__=='__main__':raise SystemExit(main())
