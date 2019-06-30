

import re
import requests
from bs4 import BeautifulSoup
import time
import cfscrape #跳过cloudflare
  
#.encode('gbk','ignore')
def writeTxt(path , txt) :
	f =  open( path ,"a"  ) 
	f.write(  txt.encode('gbk','ignore').decode('gbk','ignore')    )
	f.close()
	
 
javlibraryurl = 'http://www.javlibrary.com/tw/vl_searchbyid.php?keyword=DVDMS-414'  
#webText = scraper.get(url).text 
scraper = cfscrape.create_scraper()
webText = scraper.get(javlibraryurl).content 
   
#soup = BeautifulSoup(webText , 'lxml')  
soupjavlibrary = BeautifulSoup(webText , 'html.parser')  

imgo = soupjavlibrary.find('img' , id="video_jacket_img"   )
img = imgo['src'] 
TitleCn = soupjavlibrary.find( 'h3'    ).text.strip()

print( TitleCn )

 
#TitleCn = 'DVDMS-414 【友達ち○ぽ寝取られ】最愛の彼女が僕のいない間に大学の男友達10人のち○ぽに何度も中出しされてました… 嬉しそうにしごいてしゃぶってヌキまくっていた女子大生・はるか 21歳'

writeTxt("pachong.txt" , TitleCn  )
      
