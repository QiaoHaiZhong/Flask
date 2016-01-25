# coding=utf-8
#!/usr/bin/env python
from flask import Flask, request, render_template
import MySQLdb,sys
reload(sys)
sys.setdefaultencoding('utf-8')
app = Flask(__name__)
def oneTimeKaBi(starttime):
    con = MySQLdb.connect(host='10.10.10.39', port=3306, user='root', passwd='root', db='buyu2_all_plat',charset = "utf8")
    cur = con.cursor()
    sqlbuyu2 = "select u.puid,u.name  ,l.orderNum, l.operTime,l.operCoin from log_coin_oper l,tb_user u   where l.userId=u.id and sucFlag!=1  and type =0  and operTime>='" +  starttime + "' order by operTime desc ;"
    #sqlcb = "select u.puid,u.name,r.order_id, r.create_date,  r.coin,r.type from cb_rechange r,user u where u.id=r.user_id and type in (3,4)  and create_date >= '2015-11-3'order by create_date ;"
    print sqlbuyu2
    result = cur.execute(sqlbuyu2)
    a = cur.fetchmany(result)
    lenResult = len(a)
    if len(a) == 0 :
        print "No Data"
    calist = []
    for i in range(0, lenResult):
        ca = {}
        ca['puid'] = a[i][0]
        #print a[i][1].decode(('gbk')
        ca['name'] = (a[i][1])
        ca['orderNum'] = a[i][2]
        ca['operTime'] = a[i][3]
        ca['operCoin'] = a[i][4]
        calist.append(ca)
        del ca
    lenCalist = len(calist) 
    return calist

def twoTimeKaBi(starttime,endtime):
    con = MySQLdb.connect(host='10.10.10.39', port=3306, user='root', passwd='root', db='buyu2_all_plat',charset = "utf8")
    cur = con.cursor()
    sqlbuyu2 = "select u.puid,u.name  ,l.orderNum, l.operTime,l.operCoin from log_coin_oper l,tb_user u   where l.userId=u.id and sucFlag!=1  and type =0  and operTime>='" +  starttime + "' and  operTime<='" + endtime + "' order by operTime desc ;"
    #sqlcb = "select u.puid,u.name,r.order_id, r.create_date,  r.coin,r.type from cb_rechange r,user u where u.id=r.user_id and type in (3,4)  and create_date >= '2015-11-3'order by create_date ;"
    print sqlbuyu2
    result = cur.execute(sqlbuyu2)
    a = cur.fetchmany(result)
    lenResult = len(a)
    if len(a) == 0 :
        print "No Data"
    calist = []
    for i in range(0, lenResult):
        ca = {}
        ca['puid'] = a[i][0]
        #print a[i][1].decode(('gbk')
        ca['name'] = (a[i][1])
        ca['orderNum'] = a[i][2]
        ca['operTime'] = a[i][3]
        ca['operCoin'] = a[i][4]
        calist.append(ca)
        del ca
    lenCalist = len(calist) 
    return calist

def stringSql(sql):
    con = MySQLdb.connect(host='10.10.10.39', port=3306, user='root', passwd='root', db='buyu2_all_plat',charset = "utf8")
    cur = con.cursor()
    #sqlbuyu2=sql
    #sqlbuyu2 = "select u.puid,u.name  ,l.orderNum, l.operTime,l.operCoin from log_coin_oper l,tb_user u   where l.userId=u.id and sucFlag!=1  and type =0  and operTime>='" +  starttime + "' order by operTime desc ;"
    #sqlcb = "select u.puid,u.name,r.order_id, r.create_date,  r.coin,r.type from cb_rechange r,user u where u.id=r.user_id and type in (3,4)  and create_date >= '2015-11-3'order by create_date ;"
    #print sqlbuyu2
    result = cur.execute(sql)
    a = cur.fetchmany(result)
    lenResult = len(a)
    if len(a) == 0 :
        print "No Data"
    calist = []
    for i in range(0, lenResult):
        ca = {}
        ca['puid'] = a[i][0]
        #print a[i][1].decode(('gbk')
        ca['name'] = (a[i][1])
        ca['orderNum'] = a[i][2]
        ca['operTime'] = a[i][3]
        ca['operCoin'] = a[i][4]
        calist.append(ca)
        del ca
    lenCalist = len(calist) 
    return calist

@app.route('/')
def index():
    return render_template("query.html")
@app.route('/oneTime', methods=['POST', 'GET'])
def oneTime():
    if request.method == 'POST':
        oneStartTime = request.form['oneStartTime']
        print oneStartTime
        result=oneTimeKaBi(oneStartTime)
        lenCalist=len(result)
        return render_template('buyuquery.html', calist=result, lenCalist=lenCalist)
    else:
        lenCalist=0
        result=[]
        return render_template('buyuquery.html', calist=result, lenCalist=lenCalist)
    #return render_template('message.html', calist=result, lenCalist=lenCalist)
@app.route('/twoTime', methods=['POST', 'GET'])
def twoTime():
    if request.method == 'POST':
        twoStartTime = request.form['twoStartTime']
        twoEndTime = request.form['twoEndTime']
        #print oneStartTime
        result=twoTimeKaBi(twoStartTime,twoEndTime)
        lenCalist=len(result)
    return render_template('message.html', calist=result, lenCalist=lenCalist)

@app.route('/textSql', methods=['POST', 'GET'])
def strisdsdngSql():
    if request.method == 'POST':
        sql = request.form['textSql']
        
        print sql
        result=stringSql(sql)
        lenCalist=len(result)
    return render_template('message.html', calist=result, lenCalist=lenCalist)  
@app.route('/kabi')
def kabi():
    return render_template('query.html')
    #return render_template('message.html', calist=calist, lenCalist=lenCalist)
    
@app.route('/home')
def home():
    return render_template('admin.html')
    
@app.route('/admin')
def adminIndex():
    return render_template('admin.html')
  
@app.route('/buyuquery')
def buyuquery():
    return render_template('buyuquery.html')  

@app.route('/cbquery')
def query():
    return render_template('cbquery.html') 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
