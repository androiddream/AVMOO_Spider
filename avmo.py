# -*- coding: UTF-8 -*-    
#!/usr/bin/env python

__auther__ = 'xiaohuahu94@gmail.com'

import urllib,urllib2
import sys,time 
import os
import re
import requests
global fail_sum
def SaveImage(addr):
  try:	
  	headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   }    
 	u=requests.get(addr,headers=headers)
 	data = u
 	splitPath = addr.split('/')
 	fName = splitPath.pop()
 	now = time.strftime("%Y-%m-%d %H:%M:%S")
	print fName,'saved',now
	sentence = " osascript -e 'display notification \"lol\" with title \"Completed\"' "
	os.system(sentence)
	f= open(fName,'wb')
 	f.write(data.content)
 	f.close()
  except Exception,e:
 	print 'failed :'+str(e)

def GetOne(head,tail):
 time.sleep(0.5)
 url = 'https://avmo.pw/en/search/'
 xx=str(tail)
 key = str(head) + str(tail)
 print '%s downloading...'%key
 key_len=len(key)
 unicode(key,'utf-8')
 url = url + key
 req = urllib2.Request(url)
 req.add_header('User-Agent','Mozilla 5.10')
 fo = urllib2.urlopen(req)
 html = str(fo.read())


 wait = re.compile(r'https://jp\.netcdn\.space/digital/video/[a-z0-9]+/[a-z0-9]+\.jpg')
 image1 =re.findall(wait,html)
 r_detail = re.compile(r'https://avmo\.pw/en/movie/[0-9a-z]+')
 image_detail = re.findall(r_detail,html)
 if(image_detail==[]):
  print 'failed'
  global fail_sum
  fail_sum = 0
  fail_sum = fail_sum + 1
  return
 s = image_detail[0]

 req2 = urllib2.Request(s)
 req.add_header('User-Agent','Mozilla 5.10')
 fod = urllib2.urlopen(req2)
 html2 = str(fod.read())
 wait2 = re.compile(r'https://jp\.netcdn\.space/digital/video/[a-zA-Z0-9]+/[a-zA-Z0-9]+pl\.jpg')

 big_image = re.findall(wait2,html2)
 if (big_image==[]):
  print 'empty'
  global fail_sum
  fail_sum = fail_sum + 1
  return
 addr = big_image[0]
 SaveImage(addr)

def GetHead(key):  #get the letter string  of the keyword
	if key[3] < 'A':
		return key[0:3]
	elif key[4]<'A':
	    return key[0:4]
	else:
		return key[0:5]
def GetTail(key): #get the number  string of the keyword
	if (key[3] < 'A'):
		return key[3:len(key)]
	elif key[4]<'A':
	    return key[4:len(key)]
	else:
	    return key[5:len(key)]

def main():
	if sys.argv[1].startswith('--'):     
		option = sys.argv[1][2:]     
		# fetch sys.argv[1] but without the first two characters     
		if (option == 'version'): 
		    print 'Version 1.2'    
		elif (option == 'help'):     
		    print '格式:python avmo.py iptd555\n不支持番号中的"-"\n自动向上循环搜索,人工介入或10次失败自动退出'
	else:
	    key = sys.argv[1]
	    if(len(key)<6 ):
	    	print "番号长度太短"
	    	sys.exit()
	    print 'Thank avmo.pw a lot'
	    head = GetHead(key)
	    tail = int(GetTail(key))
        while(1):
	       GetOne(head,tail)
	       tail = tail + 1
	       # global fail_sum
	       # if fail_sum>10:
	       # 	print '此系列已到最大'
	       #  sys.exit()
if __name__ == '__main__':
	main()

