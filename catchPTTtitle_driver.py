import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import collections
from operator import itemgetter

#url = 'https://www.ptt.cc/bbs/Beauty/index.html'
url = 'https://www.ptt.cc/bbs/Tech_Job/index.html'
driver = webdriver.Chrome(executable_path='C:\\Users\\Hungyu Wei\\Downloads\\chromedriver.exe')  # PhantomJs
driver.get(url)
pageSource = driver.page_source
soup = BeautifulSoup(pageSource,"lxml")
dict_collect = {}
#print("dict_collect",dict_collect)
num_page = 2
while(num_page > 0):
    childs = soup.select('.r-list-container')[0].children
    for child in childs:
        #print(child)
        if(child.name is not None):
            if(child['class'][0] == "r-list-sep"):
                break;
            else:
                #print(child['class'])
                #print(type(child.find('a')))
                #print("item.nextSibling",child.next_siblings)
                if(child.find('a') is not None):
                    referenceTitle = child.select('.title')[0].text
                    #print(referenceTitle, child.select('.author')[0].text)
                    refrenceUrl = 'https://www.ptt.cc'+child.find('a')['href']
                    #print(refrenceUrl)
                    reference_rate_obj = child.find("span",{"class":["f3","f2","f1"]})
                    if(reference_rate_obj is not None):
                        reference_rate = reference_rate_obj.get_text()
                        if(reference_rate == "爆"):
                            reference_rate = 100
                        temp_key = referenceTitle + '\n' + refrenceUrl
                        dict_collect[temp_key] = int(reference_rate)
                        #print(reference_rate)
                    driver.get('https://www.ptt.cc'+child.find('a')['href'])
                    pageSource = driver.page_source
    #print("dict_collect",dict_collect)
    #print("--------------------------------")
    num_page = num_page-1
    #print("next page")
    prePage = soup.find("div",{"class":"btn-group","class":"btn-group-paging"}).findChildren()[1]
    urlPrepage = prePage['href']
    #print(urlPrepage)
    driver.get("https://www.ptt.cc"+urlPrepage)
    pageSource = driver.page_source
    soup = BeautifulSoup(pageSource,"lxml")
dict_order = collections.OrderedDict(sorted(dict_collect.items(), key=itemgetter(1), reverse=True))
#print(dict_order)
for k, v in dict_order.items():
    print(k, v)
'''
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
'''
