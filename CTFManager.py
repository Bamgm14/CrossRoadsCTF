import os
import multiprocessing as m
import docker as d
import time as t
import sys
from getpass import getpass
threads=[]
client=d.from_env()
settupinfo={'ip':'0.0.0.0','cport':8000,'bport':31337,'time':300,'username':None,'password':None,'docker':False}
try:
    if sys.platform=='linux':
        try:
            os.system('service mysql start')
        except:
            pass
    os.system('''mysql -e "create user toor identified by 'toor'"''')
    print('MYSQL Username and Password is toor')
except:
    pass
def Clear():
    while True:
        if os.system('clear')==1:
            os.system('cls')
        t.sleep(settupinfo['time'])
def Check(lst):
    for x in lst:
        if x.lower().endswith('.py'):
            if sys.platform=='linux':
                return '"/bin/python3 '+x+'"'
            return '"python3 '+x+'"'
        elif x.lower().endswith('.elf') and sys.platform=='linux':
            return r"./"+x
        elif x.lower().endswith('.exe') and sys.platform=='win32':
            return r"./"+x
def StartServer(info):
    print('Start')
    lst=[]
    with open("CrossRoads/Constant.py",'w') as f:
        Constant='''user="{0}"
password="{1}"
ip="{2}"
'''
        f.write(Constant.format(info['username'],info['password'],info['ip']))
    os.system('cd CrossRoads && python3 manage.py runserver '+str(info['ip'])+':'+str(info['cport']))
def StartBackGround(x,info):
    print('Start')
    os.system('cd Background/'+os.listdir(os.getcwd()+r'/Background')[x]+' && ncat -lvk '+str(info['ip'])+' '+str(info['bport']+x)+' -e '+str(Check(os.listdir(os.getcwd()+r'/Background/'+os.listdir(os.getcwd()+r'/Background')[x]))))
def Start(info):
    threads.append(('Server',m.Process(target=StartServer,args=(info,))))
    for x in range(len(os.listdir(os.getcwd()+r'/Background'))):
        threads.append(('Back'+str(x+1),m.Process(target=StartBackGround,args=(x,info))))
    threads.append(('Clear',m.Process(target=Clear)))
    for x in threads:
        print(x[0]+' Starting Up')
        x[1].start()
if __name__ == "__main__":
    print("CTFManager:The Manager For This CTF")
    if "--help" in sys.argv or "-h" in sys.argv:
        print("""
        python3 CTFManager.py --ip="<ip address>" --cport=<website port> --bport=<background port range> --screen-wipe=<time delay> --mysqluser="<username>" --mysqlpassword="<password>"[Not Adviced]
        Options:
        --ip/-i [IP Address Going To Be Used (Default=127.0.0.1)]
        --cport/-c [Website Connection Port (Default=8000)]
        --bport/-b [Background Port Range, by adding ports to background programs (Default=31337)]
        --screen-wipe/-sw [Clears The Screen Of Excess Data]
        --mysqluser/-mu [MySQL Username]
        --mysqlpassword/-mp [MySQL Password]
        --dockermode/-d [Start a Docker Envirnment]
        """)
        sys.exit(0)
    for x in sys.argv:
        if '--ip' in x or '-i' in x:
            settupinfo['ip']=x.split('=')[1]
        elif '-b' in x or '--bport' in x:
            settupinfo['bport']=x.split('=')[1]
        elif '-c' in x or '--cport' in x:
            settupinfo['cport']=x.split('=')[1]
        elif '-sw' in x or '--screen-wipe' in x:
            settupinfo['time']=x.split('=')[1]
        elif '-mu' in x or '--mysqluser' in x:
            settupinfo['username']=x.split('=')[1]
        elif '-mp' in x or '--mysqlpassword' in x:
            print("[!]WARNING:It is not advised to put password in command line")
            settupinfo['password']=x.split('=')[1]
        elif '-d' in x:
            settupinfo['docker']=True
    if not settupinfo['username']:
        settupinfo['username']=input("MySQL Username:")
    if not settupinfo['password']:
        settupinfo['password']=getpass('MySQL Password:')
    if not settupinfo['docker']:
        Start(settupinfo)
    if settupinfo['docker']:
        os.system('docker build -t ctfmanager .')
        client.containers.run('ctfmanager','python3 CTFManager.py -mu={0} -mp={1}'.format(settupinfo['username'],settupinfo['password']),detach=True,ports={'{0}/tcp'.format(x):x for x in [settupinfo['cport']]+[settupinfo['bport']+x for x in range(len(os.listdir(os.getcwd()+r'/Background')))]})
        
    

