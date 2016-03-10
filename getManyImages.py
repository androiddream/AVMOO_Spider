#!/usr/bin/env python

#coding :UTF-8

__auther__ = 'mashaz'

import urllib,urllib2
import sys,time 
import re
print 'Thank JAZMOO a lot'

x=803
while(1):
 time.sleep(0.5)
 url = 'http://www.javmoo.xyz/en/search/'
 if(x==988):break
 xx=str(x)
 x = x+1
 key = 'mibd-' +xx
 print '%s downloading...'%key
 key_len=len(key)
 unicode(key,'utf-8')
 url = url + key
 req = urllib2.Request(url)
 req.add_header('User-Agent','Mozilla 5.10')
 fo = urllib2.urlopen(req)
 html = str(fo.read())
 #print html

 wait = re.compile(r'http://d8c5bb17\.ds\.netcdn\.xyz/digital/video/[a-z0-9]+/[a-z0-9]+\.jpg')
 image1 =re.findall(wait,html)
 #print image1[0]

 
 r_detail = re.compile(r'http://www\.javmoo\.xyz/en/movie/[a-zA-Z0-9]+')

 image_detail = re.findall(r_detail,html)
 if(image_detail==[]):
  print 'failed'
  continue
 s = image_detail[0]
 #print s
 #s detail_web

 req2 = urllib2.Request(s)
 req.add_header('User-Agent','Mozilla 5.10')
 fod = urllib2.urlopen(req2)
 html2 = str(fod.read())
 if(key_len==7):
  wait2 = re.compile(r'http://d8c5bb17\.ds\.netcdn\.xyz/digital/video/[a-zA-Z0-9]+/[0-9]{0,3}[a-z]{3}00[0-9]{3}pl\.jpg')
 if(key_len==8):
  wait2 = re.compile(r'http://d8c5bb17\.ds\.netcdn\.xyz/digital/video/[a-zA-Z0-9]+/[0-9]{0,3}[a-z]{4}00[0-9]{3}pl\.jpg')
 

 big_image = re.findall(wait2,html2)
 if (big_image==[]):
  print 'failed'
  continue
 #print big_image[0]
 #print html2

 def getImage(addr):
  try:	
 	u = urllib2.urlopen(addr,timeout=10)#timeout DONE
 	data=u.read()
 	splitPath = addr.split('/')
 	fName = splitPath.pop()
 	now = time.strftime("%Y-%m-%d %H:%M:%S")
 	print fName,'saved',now
 
 	f= open(fName,'wb')
 	f.write(data)
 	f.close()
  except Exception,e:
 	print 'failed'+str(e)
 addr = big_image[0]
 getImage(addr)
