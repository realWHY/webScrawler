import requests
import time
from bs4 import BeautifulSoup as bs

payload = {
    'revAvailabilitySearch.SearchInfo.AdultCount':'1',
    'revAvailabilitySearch.SearchInfo.ChildrenCount':'0',
    'revAvailabilitySearch.SearchInfo.InfantCount':'0',
    'revAvailabilitySearch.SearchInfo.Direction':'Return',
    'revAvailabilitySearch.SearchInfo.PromoCode':'',
    'revAvailabilitySearch.SearchInfo.SalesCode':'',
    'revAvailabilitySearch.SearchInfo.SearchStations[0].DepartureStationCode':'TPE',
    'revAvailabilitySearch.SearchInfo.SearchStations[0].ArrivalStationCode':'CTS',
    'revAvailabilitySearch.SearchInfo.SearchStations[0].DepartureDate':'04/06/2017',
    'revAvailabilitySearch.SearchInfo.SearchStations[1].DepartureStationCode':'CTS',
    'revAvailabilitySearch.SearchInfo.SearchStations[1].ArrivalStationCode':'TPE',
    'revAvailabilitySearch.SearchInfo.SearchStations[1].DepartureDate':'04/06/2017',
}

rs = requests.session()
res1 = rs.post("http://makeabooking.flyscoot.com/Book/?culture=zh-tw", data = payload)
time.sleep(3)
res2 = rs.get("http://makeabooking.flyscoot.com/Book/Flight")

bsObj = bs(res2.text)
info = bsObj.findAll("div",{"class":"tab-area"})
depart = info[0]
back = info[1]
print("\ndepart time is : \n")
print(depart)
print("\nback time is : \n")
print(back)
