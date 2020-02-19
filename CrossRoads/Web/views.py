from django.shortcuts import render
import mysql.connector as m
def chal1(request):
    row=''
    e='No Errors'
    mydb=m.connect(host="localhost",
    user="root",
    passwd="bamgm146",
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
    row=''
    e='No Errors'
    mydb=m.connect(host="localhost",
    user="root",
    passwd="bamgm146",
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
