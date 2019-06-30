'''
import requests
from bs4 import BeautifulSoup
import cfscrape 
from func_pachong import *  


def getWeb(url):
	"""
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
	}
	r =  requests.get( url  , headers=headers  )
	r.encoding = "utf-8"
	cc = r.text 
	"""
	scraper = cfscrape.create_scraper()
	cc = scraper.get(url).content
	writeTxt("log.txt" , str(cc)  )	
	soup = BeautifulSoup(cc, 'lxml')
	return soup 
	
#soup.find_all('section' , 'grid__item' )
sp = getWeb(  'https://live.kuaishou.com/u/3xp7up4gtv4nme2/3xka3feas4asig9?did=web_5accef3b9f7bf2489d3f4f03ebd1e530'  )

videos = sp.find_all('video' )

print(videos)
'''

 
	
	

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from func_pachong import *  
from bs4 import BeautifulSoup
import time

 
 
 
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path='E:\\repositories\\chromedriver_win32\\chromedriver' , options=chrome_options )
 

driver.get( 'https://live.kuaishou.com/u/3xp7up4gtv4nme2/3xka3feas4asig9?did=web_5accef3b9f7bf2489d3f4f03ebd1e530' )


'''
video = driver.find_element_by_tag_name('video')

print(video)
 
new_list = browser.find_element_by_id('new_list')
user_name = browser.find_element_by_name ('user_name')
active = browser.find_element_by_class_name  ('active')
p = browser.find_element_by_tag_name ('p')

# find_element_by_name 通过name查找单个元素
# find_element_by_xpath 通过xpath查找单个元素
# find_element_by_link_text 通过链接查找单个元素
# find_element_by_partial_link_text 通过部分链接查找单个元素
# find_element_by_tag_name 通过标签名称查找单个元素
# find_element_by_class_name 通过类名查找单个元素
# find_element_by_css_selector 通过css选择武器查找单个元素
# find_elements_by_name 通过name查找多个元素
# find_elements_by_xpath 通过xpath查找多个元素
# find_elements_by_link_text 通过链接查找多个元素
# find_elements_by_partial_link_text 通过部分链接查找多个元素
# find_elements_by_tag_name 通过标签名称查找多个元素
# find_elements_by_class_name 通过类名查找多个元素
# find_elements_by_css_selector 通过css选择武器查找多个元素

'''


for i in range(1, 5):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
	
cc = driver.page_source
 
print(cc) 
 
soup = BeautifulSoup(cc, 'lxml')

videos = soup.find_all('video' )

#print(videos) 
 
 