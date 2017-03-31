import requests
from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome(executable_path='C:\\Users\\Hungyu Wei\\Downloads\\chromedriver.exe')  # PhantomJs
driver.get('http://www.xinshipu.com/zuofa/49391')
pageSource = driver.page_source
soup = BeautifulSoup(pageSource,"lxml")
#print(soup)
reup = soup.select('.re-up')[0]
#print(reup)
print(reup.select('.no-overflow')[0].text)
print(reup.select('.col')[0].text)
print(reup.select('.col')[1].text)
print(reup.select('.mt12 span:nth-of-type(2)')[0].text)
print(reup.select('.mt12 span:nth-of-type(4)')[0].text)