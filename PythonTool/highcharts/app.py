#coding=utf-8
from flask import Flask,request,render_template
import json,urllib,random
app=Flask(__name__)

@app.route('/dongtai')
def dongtai():
    text={}
   # title = {text: '月平均气温' }
    a=random.randint(0,20)
    return render_template('/tuofang.html')

@app.route('/')
def index():
    text={}
   # title = {text: '月平均气温' }
    title=json.dumps({'text':"city templature"})
    print title

    #a={ categories: ['2015-12-01', '2015-12-02', '2015-12-03', '四月', '五月', '六月' ,'七月', '八月', '九月', '十月', '十一月', '十二月']}
    return render_template('/index.html',title=title)

@app.route('/bing')
def bing():
    f=open('static/ip.list')
    iplist=f.readlines()
    areadic={}
    for i in range(0,len(iplist)):
        ip=iplist[i].strip('\n')
        url='http://ip.taobao.com/service/getIpInfo.php?ip='+ ip
        response=urllib.urlopen(url).read() 
        jsondata=json.loads(response)

        ip=jsondata[u'data'][u'ip']
        city=jsondata[u'data'][u'city'].encode('utf-8')
        area_id=jsondata[u'data'][u'area_id']
        area=jsondata[u'data'][u'area'].encode('utf-8')
        country=jsondata[u'data'][u'country'].encode('utf-8')
        region=jsondata[u'data'][u'region'].encode('utf-8')
        isp=jsondata[u'data'][u'isp'].encode('utf-8')
        num=1
        #areadic.setdefault(region,num)
        if region in areadic.iterkeys():
            areadic[region]= areadic[region]+1
        else:
            areadic.setdefault(region,num)
        #print country, isp ,area, region , city

    f.close()    
    data=[]
    for k,v in areadic.iteritems():
        c=[]
        c.append(k)
        c.append(v)
        data.append(c)
   
    #print areadic 
    for k,v in areadic.iteritems():
        print k,v
    print data
    tudata=json.dumps(data, ensure_ascii=False).decode('utf8')

    return render_template('ipbing.html',abcde=tudata)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8082, debug=True)