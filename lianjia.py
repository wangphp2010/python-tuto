import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2669.400 QQBrowser/9.6.10990.400',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Referer':'https://www.baidu.com/link?url=znRkKNPxTXXmN7m4lWy28vWXLWyx_hTEW4bLC5Pi8YR_s5wAdQk4FExi8Fz6HxHc&wd=&eqid=f2ad9a7e00007f1200000004594a3116'         
}
urls = [] # 定义空列表，用于创建所有的爬虫链接

#基于for循环，构造完整的爬虫链接
for i in ['zufang']:
    url = 'http://sh.lianjia.com/%s/' %i       
    for j in list(range(1,101)): 
        urls.append('http://sh.lianjia.com/%s/pg%s/' %(i,j)) #拼接所有需要爬虫的链接


#print(urls)


 
#创建csv文件，用于后面的保存数据
file = open('C:/Users/user/Desktop/python/lianjia.csv','w')

def readpage(url):
    try:
        res = requests.get(url , headers=headers)
    except ConnectionError as e:
        return None
    return res

def viewsubway(res2):
    try:
        view = res2.find_all('span',{'class':'fang-subway-ex'})[0].find_all('span')[0].text
    except IndexError as e:
        return None
    return view

for url in urls: #基于for循环，抓取出所有满足条件的标签和属性列表，存放在find_all中
    res = readpage(url )
    res = res.text.encode(res.encoding).decode('utf-8')
    soup = BeautifulSoup(res,'html.parser')
    find_all = soup.find_all(name = 'div',attrs = {'class':'content__list--item'})  
    
     


    for i in list(range(len(find_all))):  #基于for循环，抓取出所需的各个字段信息
        title = find_all[i].find('a')['title'] #每套租房的标语
        print( title)
        break   
        res2 = find_all[i]
        name = res2.find_all('div',{'class':'where'})[0].find_all('span')[0].text #租房所在的小区名称
        room_type = res2.find_all('div',{'class':'where'})[0].find_all('span')[1].text #租房的户型
        size = res2.find_all('div',{'class':'where'})[0].find_all('span')[2].text[:-3]#租房的面积

        #采用列表解析式，删除字符串的首位空格
        info = [i.strip() for i in res2.find_all('div',{'class':'con'})[0].text.split('\n')]
        region = info[1] #租房所在的区
        area = info[2] #租房所在的街道地域
        louceng = info[4][:2] #租房所在的楼层
        chaoxiang = info[7][3:] #租房的朝向 

        #每套租房的租金
        price = res2.find_all('div',{'class':'price'})[0].find_all('span')[0].text
        
        #地铁站及地铁
        view = viewsubway(res2)
        if view != None:
            subway = view[2:5] #租房附近的地铁线
            distance = view[-4:-1] #租房到地铁站的距离
        else:
            subway = '\0'
            distance = '\0'
        
        #将上面的各字段信息值写入并保存到csv文件中
        file.write(','.join((name.encode('gbk','ignore'),room_type.encode('gbk','ignore'),size.encode('gbk','ignore'),region.encode('gbk','ignore'),area.encode('gbk','ignore'),louceng.encode('gbk','ignore'),chaoxiang.encode('gbk','ignore'),price.encode('gbk','ignore'),subway.encode('gbk','ignore'),distance.encode('gbk','ignore'),title.encode('gbk','ignore'))) + '\n')
    break
#关闭文件(否则数据不会写入到csv文件中)
file.close()
 
