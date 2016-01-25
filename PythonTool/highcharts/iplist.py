#coding=utf-8
import urllib,json,time
f=open('static/ip.list')
iplist=f.readlines()
areadic={}
for i in range(0,len(iplist)):
    ip=iplist[i].strip('\n')
    url='http://ip.taobao.com/service/getIpInfo.php?ip='+ ip
    response=urllib.urlopen(url).read() 
    jsondata=json.loads(response)  
    print jsondata
    #print response
    ip=jsondata[u'data'][u'ip']
    city=jsondata[u'data'][u'city'].encode('utf-8')
    #print city.encode('utf-8')
    area_id=jsondata[u'data'][u'area_id']
    area=jsondata[u'data'][u'area'].encode('utf-8')
    country=jsondata[u'data'][u'country'].encode('utf-8')
    region=jsondata[u'data'][u'region']
    isp=jsondata[u'data'][u'isp'].encode('utf-8')
    #areadic[regsion]=1
    num=1
    #areadic.setdefault(region,num)
    if region in areadic.iterkeys():
        areadic[region]= areadic[region]+1
    else:
        areadic.setdefault(region,num)
        
    #print areadic
    #print country, isp ,area, region , city
    #print region 

    #time.sleep(2)
f.close()

for k, v in areadic.iteritems():
    print k.encode('utf-8'),v
total=0  
for  v in areadic.values():
    total = total +v
    
#print total

data=[]
for k,v in areadic.iteritems():
    c=[]
    c.append(k)
    c.append(v)
    data.append(c)
   
print areadic 
print data
    
