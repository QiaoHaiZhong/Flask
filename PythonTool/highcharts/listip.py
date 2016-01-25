#coding=utf-8
def iplist():
    ip1='220.160.0.0'
    ip2='220.191.255.255'
    a1=int(ip1.split('.')[0])
    a2=int(ip1.split('.')[1])
    a3=int(ip1.split('.')[2])
    a4=int(ip1.split('.')[3])
    b1=int(ip2.split('.')[0])
    b2=int(ip2.split('.')[1])
    b3=int(ip2.split('.')[2])
    b4=int(ip2.split('.')[3])
    
    print a1,a2,a3,a4
    print b1,b2,b3,b4
    
    num=0
    for i in range(a4,b4+1):
        for j in range(a3,b3+1):
            for k in range(a2,b2+1):
                for l in range(a1,b1+1):
                    num=num+1
                    print str(a1)+'.'+str(k)+'.'+str(j)+'.'+str(i) +'===='+str(num)