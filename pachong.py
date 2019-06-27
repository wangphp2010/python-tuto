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
url = "https://watchjavonline.com/" 
r = requests.get(url)

print ("获取特定的URL地址")
soup = BeautifulSoup(r.text, 'lxml')
#https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#contents-children
#soup = BeautifulSoup(r.text,  "html.parser",from_encoding="utf-8")
sections = soup.find_all('section' , 'grid__item' )
 
#print(sections)

def writeTxt(path , txt) :
	f=  open( path ,"a") 
	f.write( txt  )
	f.close()
	

preg_l = '' ;
preg_l += '([a-zA-Z][a-zA-Z0-9]+\-[a-zA-Z0-9]+\d+)';
preg_l +='|((Tokyo Hot\s*)((\d*[a-zA-Z0-9]+\-\d+)|([a-zA-Z][0-9]+)))';
preg_l +='|(^[a-zA-Z0-9]+\s\d+\-[a-zA-Z]+\d+)';
preg_l +='|(S-Cute[\w\s\-\_]+)';
	
	
	
def getCatId(title)   :
	if re.search( r"face" ,  title , re.IGNORECASE )   :  
		catId = 29
	elif(re.search( "cute", title , re.IGNORECASE ) ) : 
		catId = 42  
	elif(re.search( "S-CUTE", title , re.IGNORECASE ) ) : 
		catId = 42  
	elif(re.search( "女子校生", title , re.IGNORECASE ) ) : 
		catId = 33  
	elif(re.search( "Niece", title , re.IGNORECASE ) ) : 
		catId = 36  
	elif(re.search( "Mouths", title , re.IGNORECASE ) ) : 
		catId = 29  
	elif(re.search( "Housemaid", title , re.IGNORECASE   ) ) : 
		catId = 40  
	elif(re.search( "Humiliation", title , re.IGNORECASE ) ) : 
		catId = 28 
	elif(re.search( "wife", title , re.IGNORECASE ) ) : catId = 32 
	elif(re.search( "Married Woman", title , re.IGNORECASE ) ) : 
		catId = 32 
	elif(re.search( "Schoolgirl", title , re.IGNORECASE ) ) : 
		catId = 33 
	elif(re.search( "Mother", title , re.IGNORECASE ) ) : 
		catId = 36 
	elif(re.search( "father", title , re.IGNORECASE ) ) : 
		catId = 36 
	elif(re.search( "brother", title , re.IGNORECASE ) ) : 
		catId = 36 
	elif(re.search( "sister", title , re.IGNORECASE ) ) : 
		catId = 36 
	elif(re.search( "teacher", title , re.IGNORECASE ) ) : 
		catId = 37 
	elif(re.search( "rape", title , re.IGNORECASE ) ) : 
		catId = 39 
	elif(re.search( "cute", title , re.IGNORECASE ) ) : 
		catId = 42  
	elif(re.search( "Mature", title , re.IGNORECASE ) ) : 
		catId = 24 
	elif(re.search( "Pregnant", title , re.IGNORECASE ) ) : 
		catId = 24 
	elif(re.search( "Bibian", title , re.IGNORECASE ) ) : 
		catId = 43 
	elif(re.search( "Lesbian", title , re.IGNORECASE ) ) : 
		catId = 43 
	elif(re.search( " Maid ", title , re.IGNORECASE ) ) : 
		catId = 34 
	elif(re.search( "Big Tits", title , re.IGNORECASE   ) ) : 
		catId = 16 
	elif(re.search( "Creampie", title , re.IGNORECASE ) ) : 
		catId = 22 
	elif(re.search( "Molester",  title , re.IGNORECASE   ) ) : 
		catId = 31  
	elif(re.search( "Molested",  title , re.IGNORECASE   ) ) : 
		catId = 31  
	elif(re.search( "Humiliation", title , re.IGNORECASE ) ) : 
		catId = 28 
	elif(re.search( "wife", title , re.IGNORECASE ) ) : 
		catId = 32 
	elif(re.search( "Married Woman", title , re.IGNORECASE ) ) : 
		catId = 32 
	elif(re.search( "Schoolgirl", title , re.IGNORECASE ) ) : 
		catId = 33 
	elif(re.search( "Mother", title , re.IGNORECASE ) ) : 
		catId = 36 
	elif(re.search( "father", title , re.IGNORECASE ) ) : 
		catId = 36 
	elif(re.search( "brother", title , re.IGNORECASE ) ) : 
		catId = 36 
	elif(re.search( "sister", title , re.IGNORECASE ) ) : 
		catId = 36 
	elif(re.search( "teacher", title , re.IGNORECASE ) ) : 
		catId = 37 
	elif(re.search( "rape", title , re.IGNORECASE ) ) : 
		catId = 39 
	elif(re.search( "cute", title , re.IGNORECASE ) ) : 
		catId = 42  
	elif(re.search( "Mature", title , re.IGNORECASE ) ) : 
		catId = 24 
	elif(re.search( "Pregnant", title , re.IGNORECASE ) ) : 
		catId = 24 
	elif(re.search( "Bibian", title , re.IGNORECASE ) ) : 
		catId = 43 
	elif(re.search( "Lesbian", title , re.IGNORECASE ) ) : 
		catId = 43 
	elif(re.search( " Maid ", title , re.IGNORECASE ) ) : 
		catId = 34 
	elif(re.search( "Big Tits", title , re.IGNORECASE ) ) : 
		catId = 16 
	elif(re.search( "Creampie", title , re.IGNORECASE ) ) : 
		catId = 22 
	elif(re.search( "Molester", title , re.IGNORECASE ) ) : 
		catId = 31  
	elif(re.search( "Molester", title , re.IGNORECASE ) ) : 
		catId = 31  
	elif(re.search( "Pervert", title , re.IGNORECASE ) ) : 
		catId = 31  
	elif(re.search( "Uniform", title , re.IGNORECASE ) ) : 
		catId = 19  
	elif(re.search( "Adolescent", title , re.IGNORECASE ) ) : 
		catId = 33  
	elif(re.search( "Middle\-aged", title , re.IGNORECASE ) ) : 
		catId = 24  
	elif(re.search( "Clinic", title , re.IGNORECASE ) ) : 
		catId = 35 
	elif(re.search( "Housewife", title , re.IGNORECASE ) ) : 
		catId = 40 
	elif(re.search( "\bass\b", title , re.IGNORECASE ) ) : 
		catId = 17  
	else  :
		catId = 21 
				
	return str(catId)
# end getCatId()	
			
			
			
for section in sections :

	img = section.img['src'].strip()
	title = section.h2.text .strip()
	href = section.a['href'].strip()
	
	if href is not None :
		r2 = requests.get(href)
		soup2 = BeautifulSoup(r2.text, 'lxml')
		iframe = soup2.find('iframe')
		vs = iframe['src'].strip()
		
		 
	fanhao = re.sub( r"preg_l", '', title ).strip()
	title = title.replace( fanhao , "" ).strip()
	
							
	if not re.search( r"\-" , fanhao ) :
		fanhao = re.sub( r"([a-zA-Z])(\d)" ,"$1-$2" ,  fanhao ) ; 
	
	title = fanhao +" "+ title  
	title = title.strip()
	cat_id = "21" 

	'''					
	print( "img" , img  )
	print( "title" , title.strip() )
	print( "href" , href )
	print( 'fanhao'  , fanhao )
	print( "vs " ,  vs )
	print("\n")
	'''
	
	print(  "adult_pic=%s <|> adult_url=%s <|>  adult_title=%s <|>  adult_cat_id=%s <|>  fanhao=%s <end> \n" % (img , vs , title , cat_id ,  fanhao )   )
	#writeTxt("pachong.txt" , "adult_pic=%s <|> adult_url=%s <|>  adult_title=%s <|>  adult_cat_id=%s <|>  fanhao=%s <end> \n" % (img , vs , title , fanhao )   )
	
	break


 
''' 
print ("正则表达式匹配")
link_node = soup.find('a',href=re.compile(r"ti"))
print (link_node.name,link_node['href'],link_node['class'],link_node.get_text())
 
print ("获取P段落的文字")
p_node = soup.find('p',class_='story')
print (p_node.name,p_node['class'],p_node.get_text())
'''