from django.shortcuts import render
cmds=['create database items',
'create database madhatter',
'use items',
'create table Food (SINo varchar(3) primary key,Item varchar(30),Price float(20,2))',
'insert into Food values("1","ComplainDX",105.00),("2","Complain",60.00),("3","Biriyani",1000.00),("4","Cheese",100.00)',
'create table password (Answer1 varchar(25) primary key,Answer2 varchar(25),Answer3 varchar(25))',
'insert into password values("CRsCTF{I_","s33_y0u_","c4n_inj3ct}")',
'use madhatter',
'create table partytoday(Person varchar(50) primary key)',
'insert into partytoday values("Alice"),("MadHatter"),("Cheshire")',
'create table password(Answer1 varchar(25) primary key,Answer2 varchar(25))',
'insert into password values("CRsCTF{B33n","_h3r3}")']
import mysql.connector as m
user='root'
password='bamgm146'
mydb=m.connect(host="localhost",
    user=user,
    passwd=password
    )
myc=mydb.cursor()
for x in cmds:
    try:
        myc.execute(x)
    except Exception as e:
        pass
mydb.commit()
def chal1(request):
    row=''
    e='No Errors'
    mydb=m.connect(host="localhost",
    user=user,
    passwd=password,
    db='items'
        )
    myc=mydb.cursor()
    cmd="select * from Food "
    q=(request.GET.get('q') or '').strip()
    if q:
        cmd+=f"where Item like '%{q}%'"
    try:
        myc.execute(cmd)
        row=myc.fetchall()
        print(row)
    except Exception as ea:
        e=ea
    context={'rows':row,'e':e,'cmd':cmd}
    return render(request,'test.html',context)
def chal2(request):
    row=''()
    e='No Errors'
    mydb=m.connect(host="localhost",
    user=user,
    passwd=password,
    db='madhatter'
        )
    myc=mydb.cursor()
    cmd="select * from partytoday "
    q=(request.GET.get('q') or '').strip().lower()
    ban=['union','select','or','database','and']
    if q:
        for x in ban:
            if x in q:
                q=q.replace(x,'')
        cmd+=f"where Person like '%{q}%'"
    try:
        myc.execute(cmd)
        row=myc.fetchall()
    except Exception as ea:
        e=ea
    context={'rows':row,'e':e,'cmd':cmd}
    return render(request,'test.html',context)
# Create your views here.
