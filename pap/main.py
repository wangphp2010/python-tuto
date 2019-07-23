import requests
from bs4 import BeautifulSoup
import cfscrape

headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
url = "https://www.pap.fr/annonce/vente-immobilier-ile-de-france-g471-1"

""" page = requests.get(url,headers=headers)
 """
scraper = cfscrape.create_scraper()
page = scraper.get(url)
 
soup = BeautifulSoup(page.content ,'html.parser')

titles = soup.find_all('span',class_="h1") 

for title in titles:
    print(title.get_text())

     