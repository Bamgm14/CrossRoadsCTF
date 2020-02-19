import os
import multiprocessing as m
import time as t
menu=''
settupinfo={'ip':'127.0.0.1','cport':8000,'bport':31337}
threads=[]
print(settupinfo)
def Check(lst):
    for x in lst:
        if x.lower().endswith('.py'):
            return '"python3 '+x+'"'
        if x.lower().endswith('.exe'):
            return x
def StartServer():
    print('Start')
    os.system('cd CrossRoads && python3 manage.py runserver '+str(settupinfo['ip'])+':'+str(settupinfo['cport']))
def StartBackGround(x):
    print('Start')
    os.system('cd Background\\'+os.listdir(os.getcwd()+r'\Background')[x]+' && ncat -lvk '+str(settupinfo['ip'])+' '+str(settupinfo['bport']+x)+' -e '+str(Check(os.listdir(os.getcwd()+r'\\Background\\'+os.listdir(os.getcwd()+r'\Background')[x]))))
def Start():
    threads.append(('Server',m.Process(target=StartServer)))
    for x in range(len(os.listdir(os.getcwd()+r'\Background'))):
        threads.append(('Back'+str(x+1),m.Process(target=StartBackGround,args=(x,))))
    for x in threads:
        print(x[0]+' Starting Up')
        print(x[1])
        x[1].start()
        print(x[1])
if __name__ == "__main__":
    Start()
