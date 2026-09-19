import json,secrets,time
from pathlib import Path
from genlayer_py import create_client,create_account
from genlayer_py.chains import studionet
R=Path(__file__).parents[1];E=(R.parents[3]/'accounts.env').read_text();v=lambda n:next(x.split('=',1)[1].strip().strip('"').strip("'") for x in E.splitlines() if x.startswith(n+'='));applicant=create_account(account_private_key=v('ACCOUNT_7_GENLAYER_PRIVATE_KEY'));institution=create_account(account_private_key='0x'+secrets.token_hex(32));ca=create_client(chain=studionet,account=applicant);ci=create_client(chain=studionet,account=institution);addr='0x35724f72864421039af8DCbD3098b0f6e23FFa16';rid='LIVE-'+str(int(time.time()));commit='30c1623';home=f'https://raw.githubusercontent.com/IDAK2/curriculum-thread/{commit}/evidence/home-syllabus.txt';target=f'https://cdn.jsdelivr.net/gh/IDAK2/curriculum-thread@{commit}/evidence/target-syllabus.txt';tx=[]
def send(client,fn,args):
 h=client.write_contract(address=addr,function_name=fn,args=args);r=client.wait_for_transaction_receipt(transaction_hash=h,status='FINALIZED',retries=180,interval=5000);assert r.get('status_name')=='FINALIZED';tx.append(h)
send(ca,'request_mapping',[rid,institution.address,'Distributed Systems',home,target,['explain consensus under partial failure','design fault-tolerant replicated services','evaluate safety and liveness tradeoffs']]);send(ci,'map_outcomes',[rid]);send(ca,'object_mapping',[rid,'https://github.com/IDAK2/curriculum-thread/blob/'+commit+'/evidence/home-syllabus.txt']);print(json.dumps({'id':rid,'state':'OBJECTED','transactions':tx}),flush=True)
