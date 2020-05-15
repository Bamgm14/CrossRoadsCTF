import os
import multiprocessing as m
import time as t
import sys
from getpass import getpass
threads=[]
settupinfo={'ip':'0.0.0.0','cport':8000,'bport':31337,'time':300,'username':None,'password':None}
def Clear():
    while True:
        if os.system('clear')==1:
            os.system('cls')
        t.sleep(settupinfo['time'])
def Check(lst):
    for x in lst:
        if x.lower().endswith('.py'):
            return '"/bin/python3 '+x+'"'
        elif x.lower().endswith('.elf'):
            return r"./"+x
        elif x.lower().endswith('.exe'):
            return r"./"+x
def StartServer():
    print('Start')
    lst=[]
    with open("CrossRoads\\Constant.py",'w') as f:
        f.write(Constant.format(settupinfo['username'],settupinfo['password'],settupinfo['ip']))
    os.system('cd CrossRoads && python3 manage.py runserver '+str(settupinfo['ip'])+':'+str(settupinfo['cport']))
def StartBackGround(x):
    print('Start')
    os.system('cd Background\\'+os.listdir(os.getcwd()+r'\Background')[x]+' && ncat -lvk '+str(settupinfo['ip'])+' '+str(settupinfo['bport']+x)+' -e '+str(Check(os.listdir(os.getcwd()+r'\\Background\\'+os.listdir(os.getcwd()+r'\Background')[x]))))
def Start():
    threads.append(('Server',m.Process(target=StartServer)))
    for x in range(len(os.listdir(os.getcwd()+r'\Background'))):
        threads.append(('Back'+str(x+1),m.Process(target=StartBackGround,args=(x,))))
    threads.append(('Clear',m.Process(target=Clear)))
    for x in threads:
        print(x[0]+' Starting Up')
        x[1].start()
if __name__ == "__main__":
    print("CTFManager:The Manager For This CTF")
    if "--help" in sys.argv or "-h" in sys.argv:
        print("""
        python3 CTFManager.py --ip="<ip address>" --cport=<website port> --bport=<background port range> --screen-wipe=<time delay>
        Options:
        --ip/-i [IP Address Going To Be Used (Default=127.0.0.1)]
        --cport/-c [Website Connection Port (Default=8000)]
        --bport/-b [Background Port Range, by adding ports to background programs (Default=31337)]
        --screen-wipe/-sw [Clears The Screen Of Excess Data]
        --mysqluser/-mu [MySQL Username]
        --mysqlpassword/-mp [MySQL Password]
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
    if not settupinfo['username']:
        settupinfo['username']=input("MySQL Username:")
    if not settupinfo['password']:
        settupinfo['password']=getpass('MySQL Password:')
    print("Settings:"+str(settupinfo))
    Start()
Constant='''
user="{0}"
password="{1}"
ip="{2}"
'''
