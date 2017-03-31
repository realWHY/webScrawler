import requests
from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome(executable_path='C:\\Users\\Hungyu Wei\\Downloads\\chromedriver.exe')  # PhantomJs
driver.get('https://www.ptt.cc/bbs/Beauty/index.html')
pageSource = driver.page_source
soup = BeautifulSoup(pageSource,"lxml")
num_page = 2
while(num_page > 0):
    for item in soup.select('.r-ent'):
        print(type(item.find('a')))
        print("item.nextSibling",item.next_siblings)
        if(item.find('a') is not None):
            print(item.select('.title')[0].text, item.select('.author')[0].text)
            print('https://www.ptt.cc'+item.find('a')['href'])
            if(item.find("span",{"class":"f3"}) is not None):
                print(item.find("span",{"class":"f3"}).get_text())
            driver.get('https://www.ptt.cc'+item.find('a')['href'])
            pageSource = driver.page_source
    num_page = num_page-1
    print("next page")
    prePage = soup.find("div",{"class":"btn-group","class":"btn-group-paging"}).findChildren()[1]
    urlPrepage = prePage['href']
    print(urlPrepage)
    driver.get("https://www.ptt.cc"+urlPrepage)
    pageSource = driver.page_source
    soup = BeautifulSoup(pageSource,"lxml")
