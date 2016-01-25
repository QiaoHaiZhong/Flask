#coding=utf-8
import  qrcode
img=qrcode.make('http://bbs.pyshell.com')
name='bbs'
img.save('./static/QrCodeImg/' + str(name) + '.png')
print 'OK'