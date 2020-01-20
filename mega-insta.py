import urllib.request as ur
from bs4 import BeautifulSoup as bs
import json
import requests as rq
import os
from random import randint,choice
from clint.textui import progress

uagent = [
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/16.04.6 Chrome/77.0.3865.120",
			'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/8.1.0.0 Safari/540.0',
			'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/8.1.0.0 Safari/540.0',
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3818.0 Safari/537.36 Edg/77.0.189.3'
		 ]
headers = {'User-Agent':choice(uagent)}

def extract(file):
    mentah = []
    mateng = []
    fopen = open(file,'r') 
    fread = fopen.read()
    imgs = fread.split("href=")
    for i in range(len(imgs)):
        if i > 0:
            mentah.append(imgs[i].split('"'))
    fopen.close()
    for i in range(len(mentah)):
        mateng.append(mentah[i][1])
    return mateng

def extUrl(url):
	req = rq.get(url, headers = headers)
	alf = req.content
	# alf = reqUrl(url)
	alf = bs(alf, 'html.parser')
	alf = alf.text
	jload = json.loads(alf)
	jload = jload["graphql"]["shortcode_media"]
	return jload

def instavid(url):
	x = extUrl(url)
	alf = x["video_url"]
	alf = rq.get(alf, stream=True)
	return alf

def instaimg(url):
	x = extUrl(url)
	alf = x["display_url"]
	alf = rq.get(alf, stream=True)
	return alf

alinks = extract('element.txt')
print('--------------------------------------------')
print('|   Instagram Video And Image Downloader   |')
print('|       github.com/megatruh/alf_inst       |')
# print('|   Instagram Video And Image Downloader   |')
print('--------------------------------------------')
print('|          Total Data Scraped :',len(alinks),'        |')
print('--------------------------------------------')
uname = str(input('Instagram Username : @'))
print('Menu Download : \n'+
	  ' 1. Image \n'+
	  ' 2. Video ')
	  # ' 3. Slide ')
choice = int(input('  >  '))

try:
	os.mkdir('mega-insta')
except:
	print('',end='')

if choice == 1:
	try:
		try:
			os.mkdir('mega-insta/%s'%(uname))
			os.mkdir('mega-insta/%s/pictures'%(uname))
		except:
			try:
				os.mkdir('mega-insta/%s/pictures'%(uname))				#LINUX
			except:
				print('')
	except:
		try:
			os.mkdirs('mega-insta\\%s'%(uname))
			os.mkdirs('mega-insta\\%s\\pictures'%(uname))
		except:
			try:
				os.mkdirs('mega-insta\\%s\\pictures'%(uname))				#WINDOWS
			except:
				print('')
elif choice == 2:
	try:
		try:
			os.mkdir('mega-insta/%s'%(uname))
			os.mkdir('mega-insta/%s/videos'%(uname))
		except:
			try:
				os.mkdir('mega-insta/%s/videos'%(uname))					#LINUX
			except:
				print('')
	except:
		try:
			os.mkdirs('mega-insta\\%s'%(uname))
			os.mkdirs('mega-insta\\%s\\videos'%(uname))
		except:
			try:
				os.mkdirs('mega-insta\\ %s\\ videos'%(uname))				#WINDOWS
			except:
				print('')

i = 1
for link in alinks:
	url = 'https://www.instagram.com'+link+'?__a=1'
	if choice == 1:
		imgs = extUrl(url)
		if imgs['__typename'] == 'GraphImage':
			image = instaimg(url)
			total_length = int(image.headers.get('content-length'))
			try :
				with open ('mega-insta/%s/pictures/%s%s.jpg'%(uname,uname,i),'wb+') as p:
				    for alf in progress.bar(image.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
				        if alf:
				            p.write(alf)
				            p.flush()
			except:
				with open ('mega-insta\\%s\\pictures\\%s%s.jpg'%(uname,uname,i),'wb+') as p:
				    for alf in progress.bar(image.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
				        if alf:
				            p.write(alf)
				            p.flush()

			p.close()
			print(' > %s%s.jpg Downloaded'%(uname,i))
		else:
			continue

	elif choice == 2:
		vids = extUrl(url)
		if vids['__typename'] == 'GraphVideo':
			video = instavid(url)
			total_length = int(video.headers.get('content-length'))
			try:
				with open ('mega-insta/%s/videos/%s%s.mp4'%(uname,uname,i),'wb+') as p:
					for alf in progress.bar(video.iter_content(chunk_size=1024), expected_size=(total_length/1024) +1):
						if alf:
							p.write(alf)
							p.flush()
			except:
				with open ('mega-insta\\%s\\videos\\%s%s.mp4'%(uname,uname,i),'wb+') as p:
					for alf in progress.bar(video.iter_content(chunk_size=1024), expected_size=(total_length/1024) +1):
						if alf:
							p.write(alf)
							p.flush()
			p.close()
			print(' > %s%s.mp4 Downloaded'%(uname,i))
		else:
			continue
	i += 1




# This program original by github.com/megatruh
# Credit me if u want recode or share
# JUST FUCKING CREDIT ME
