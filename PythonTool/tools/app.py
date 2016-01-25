# coding=utf8

from flask import Flask,request,render_template
import qrcode
import random#from qrcode.image.pure import PymagingImage
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('tools.html')

@app.route('/createQr')
def createQr():
    return render_template('/createQr.html')
@app.route('/qrcode',methods=['POST','GET'],)
def qrcode():
    if request.method=='POST':
        url=request.form['siteurl']
        print url
        imgname=url.strip('.')
        #img=qrcode.make('www.pyshell.com')
        name='a'

        #img.save('g:\\a.png')
        img=qrcode.make(url)
        img.save('static/' + imgname + '.png')
    return render_template('createQr.html')

def add(start,end,total):
    for i in range(0,total):
        a=random.randint(start+1,end+1)
        b=random.randint(start+1,end+1)
        c=random.randint(start+1,end+1)
        d=random.randint(start+1,end+1)
        e=random.randint(start+1,end+1)
        f=random.randint(start+1,end+1)
        print "%2d + %2d =        %2d + %2d =       %2d + %2d = " % (a, b, c, d, e, f)
@app.route('/add',methods=['POST','GET'])
def sum():
    if request.method=='POST':
        numStart=request.Form['startNum']
        numEnd=request.Form['endNum']
        numTotal=request.Form['totalNum']
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)