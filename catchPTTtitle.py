import requests
from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome(executable_path='C:\\Users\\Hungyu Wei\\Downloads\\chromedriver.exe')  # PhantomJs
driver.get('https://www.ptt.cc/bbs/oversea_job/index.html')
pageSource = driver.page_source
soup = BeautifulSoup(pageSource,"lxml")
for item in soup.select('.r-ent'):
    print(item.select('.title')[0].text, item.select('.author')[0].text)
    print('https://www.ptt.cc'+item.find('a')['href'])
    driver.get('https://www.ptt.cc'+item.find('a')['href'])
    pageSource = driver.page_source