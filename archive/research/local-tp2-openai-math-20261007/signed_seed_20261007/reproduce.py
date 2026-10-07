"""Rebuild exact finite certificates in isolation; not a full-tree scan."""
from pathlib import Path
import hashlib,json,subprocess,sys,tempfile,shutil,platform,datetime
ROOT=Path(__file__).resolve().parent

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
 manifest=json.loads((ROOT/'MANIFEST.json').read_text())
 for name,expected in manifest['sources'].items():
  if digest(ROOT/name)!=expected:raise RuntimeError('Source hash mismatch: '+name)
 commands=[['signed_gate.py','LRL','R'],['signed_gate.py','RLR','L'],['verify_direct.py','LRL','R'],['verify_direct.py','RLR','L'],['test_contracts.py']]
 out=ROOT/'replay_output';out.mkdir(exist_ok=True)
 runs=[];matched=0
 with tempfile.TemporaryDirectory(prefix='tp2-signed-') as temp:
  p=Path(temp)
  for name in manifest['sources']:
   if name.endswith('.py'):shutil.copy2(ROOT/name,p/name)
  for command in commands:
   r=subprocess.run([sys.executable,*command],cwd=p,capture_output=True,text=True,timeout=45)
   runs.append({'command':command,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
   if r.returncode:raise RuntimeError(r.stderr)
  for word,dr in [('LRL','R'),('RLR','L')]:
   a=json.loads((p/f'certificate_{word}_{dr}.json').read_text());b=json.loads((p/f'independent_{word}_{dr}.json').read_text())
   if a['status']!='PASS' or a['certificates']!=b['certificates']:raise RuntimeError('Certificate mismatch: '+word)
   matched+=sum(map(len,a['certificates'].values()))
  results=[]
  for name,expected in manifest['expected_results'].items():
   actual=digest(p/name)
   if actual!=expected:raise RuntimeError('Result hash mismatch: '+name)
   shutil.copy2(p/name,out/name)
   results.append({'file':name,'sha256':actual,'matches':True})
 report={'status':'PASS','scope':'Signed-seed sufficient theorem and two infinite-ray applications; full tree OPEN; mathematical claim remains PROOF_CANDIDATE','completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':platform.python_version(),'arithmetic':'Python integers and fractions.Fraction','runs':runs,'certificate_entries_matched':matched,'results':results,'independence':'Same model, separate implementations; not a fresh independent mathematical reviewer or external replication','source_hashes_match':True}
 (out/'report.json').write_text(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
 print(json.dumps({'status':report['status'],'program_runs':len(runs),'certificate_entries_matched':matched,'full_tree':'OPEN'},ensure_ascii=False))
 return 0
if __name__=='__main__':raise SystemExit(main())
