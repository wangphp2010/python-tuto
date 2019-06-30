# coding: utf-8

#import cookielib  
#import urllib2
'''
python 3以上要用
import http.cookiejar
import urllib.request
'''
'''
import http.cookiejar as cookielib
import urllib.request as urllib2
 
url = "https://watchjavonline.com/"
response1 = urllib2.urlopen(url)

print("第一种方法")

#获取状态码，200表示成功
print (response1.getcode())

#获取网页内容的长度
print (len(response1.read()))

 
print ("第二种方法")
request = urllib2.Request(url)
#模拟Mozilla浏览器进行爬虫
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print(response2.getcode())
print (len(response2.read()))
 
print ("第三种方法")
cookie = cookielib.CookieJar()
#加入urllib2处理cookie的能力
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print( response3.getcode())
print (len(response3.read()))
print (cookielib)
 '''

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import re
import requests
from bs4 import BeautifulSoup
from func_pachong import *  
import time
import cfscrape #跳过cloudflare



'''
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

#创建一个BeautifulSoup解析对象
soup = BeautifulSoup(html_doc,"html.parser",from_encoding="utf-8")
#获取所有的链接
links = soup.find_all('a')
'''
'''
print ("所有的链接")
for link in links:
    print (link.name , link['href'] , link.get_text())

'''

'''
headers = {'User-Agent': 'Mozilla/5.0'}
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

response = requests.get(url, headers=headers)  # 使用headers避免访问受限
 
soup = BeautifulSoup(response.content, 'html.parser') response.content  # 以二进制形式返回


all_a = soup.find('div',class_='postlist').find_all('a',target='_blank').find('a', rel='ff')
注意：BeautifulSoup()返回的类型是<class 'bs4.BeautifulSoup'>
find()返回的类型是<class 'bs4.element.Tag'>
find_all()返回的类型是<class 'bs4.element.ResultSet'>
<class 'bs4.element.ResultSet'>不能再进项find/find_all操作

response.status_code  # 返回状态码
response.text  #以文本格式返回网页内容
response.content  # 以二进制形式返回


soup.select('#id')
：

soup.select('a')


soup.select('.class a')

'''

 
max = 5 
catId = "21"
isTest = 1 # 是否测试


if 1 == isTest:
	max = 1 

writeTxt("pachong.txt" , ''   )

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}

 

for i in range(1, max + 1 ): # 会 1 到 max 
	uu = 'https://watchjavonline.com/page/' + str(i) + '/' 
	r =  requests.get( uu  , headers=headers  )
	r.encoding ="gbk"  
	print("获取特定的地址 %s " % uu )
	soup = BeautifulSoup(r.text, 'lxml')
	#https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#contents-children
	#soup = BeautifulSoup(r.text,  "html.parser",from_encoding="utf-8")
	sections = soup.find_all('section' , 'grid__item' )
	 
	#print(sections)
	 
		

	preg_l = '' ;
	preg_l += '([a-zA-Z][a-zA-Z0-9]+\-[a-zA-Z0-9]+\d+)';
	preg_l +='|((Tokyo Hot\s*)((\d*[a-zA-Z0-9]+\-\d+)|([a-zA-Z][0-9]+)))';
	preg_l +='|(^[a-zA-Z0-9]+\s\d+\-[a-zA-Z]+\d+)';
	preg_l +='|(S-Cute[\w\s\-\_]+)';
		
	 
				

				
				
	for section in sections :

		img = section.img['src'].strip()
		
		title = section.h2.text .strip()
		href = section.a['href'].strip()
		
		if href is not None :
			r2 = requests.get(href , headers=headers)
			r2.encoding = 'gbk' 
			soup2 = BeautifulSoup(r2.text, 'lxml')
			iframe = soup2.find('iframe')
			vs = iframe['src'].strip()
			strCat = '' 
			strCat1 = re.findall("Genre\(s\)\:([\d\D]+?)\<", r2.text )
			strCat2 = re.findall("Categories\:([\d\D]+?)\<", r2.text )
			
			if len(strCat1)>0:
				strCat += strCat1[0]
			if len(strCat2)>0:
				strCat += strCat2[0]
				    
				
			
			
			
			catId = getCatId(strCat)

			
			 
		fanhao = re.sub( r"preg_l", '', title ).strip()
		title = title.replace( fanhao , "" ).strip()
		
								
		if not re.search( r"\-" , fanhao ) :
			fanhao = re.sub( r"([a-zA-Z])(\d)" ,"$1-$2" ,  fanhao ) ; 
		
		title = fanhao +" "+ title  
		title = title.strip()
		 
		if  'fanhao' in locals().keys() and fanhao :   # 'fanhao' in locals().keys() 是否定义
			javlibraryurl = 'http://www.javlibrary.com/tw/vl_searchbyid.php?keyword=' + fanhao 
			#webText = scraper.get(url).text 
			scraper = cfscrape.create_scraper()
			webText = scraper.get(javlibraryurl).content 
			   
			#soup = BeautifulSoup(webText , 'lxml')  
			soupjavlibrary = BeautifulSoup(webText , 'html.parser')  

			imgo = soupjavlibrary.find('img' , id="video_jacket_img"   )
			  
			if imgo :
				img = imgo['src'] 
				
			TitleCn = soupjavlibrary.find( 'h3'    )
			
 			
			if TitleCn :
				TitleCn = TitleCn.text.strip()
			
			
			 
			if TitleCn : 
				title = TitleCn 
		
			
			
		'''					
		print( "img" , img  )
		print( "title" , title.strip() )
		print( "href" , href )
		print( 'fanhao'  , fanhao )
		print( "vs " ,  vs )
		print("\n")
		print(" href %s strCat %s" % ( href , strCat  ) )
		'''
		neirong = "adult_pic=%s <|> adult_url=%s <|>  adult_title=%s <|>  adult_cat_id=%s <|>  fanhao=%s <end> \n" % (img , vs , title , catId ,  fanhao )
		print(  neirong )
		writeTxt("pachong.txt" , neirong  )
		
		if 1 == isTest :
			break
			
	sleepTime = 1 		
	print("sleep for %s seconds" % sleepTime )		
	time.sleep(sleepTime)		

print('全部结束')	

 
''' 
print ("正则表达式匹配")
link_node = soup.find('a',href=re.compile(r"ti"))
print (link_node.name,link_node['href'],link_node['class'],link_node.get_text())
 
print ("获取P段落的文字")
p_node = soup.find('p',class_='story')
print (p_node.name,p_node['class'],p_node.get_text())
'''