import requests
import time
from bs4 import BeautifulSoup as bs
import datetime
import collections
from operator import itemgetter
import os

now = datetime.datetime.now()
Departure_obj = now
BackDate_obj = (now + datetime.timedelta(days = 6))

while(1):
    AdultCount = input("AdultCount: ")
    FromCountry = input("FromCountry: ")
    ToCountry = input("ToCountry: ")
    
    print('your input-> Adult count:%s, From:%s , to:%s'%(AdultCount, FromCountry, ToCountry))
    #AdultCount = '2'
    #FromCountry = 'TPE'
    #ToCountry = 'CTS'
    
    depart_dict = {}
    back_dict = {}
    for i in range(1,20):
        DepartureDate = Departure_obj.strftime('%m/%d/%Y')
        BackDate = BackDate_obj.strftime('%m/%d/%Y')
        
        payload = {
            'revAvailabilitySearch.SearchInfo.AdultCount':AdultCount,
            'revAvailabilitySearch.SearchInfo.ChildrenCount':'0',
            'revAvailabilitySearch.SearchInfo.InfantCount':'0',
            'revAvailabilitySearch.SearchInfo.Direction':'Return',
            'revAvailabilitySearch.SearchInfo.PromoCode':'',
            'revAvailabilitySearch.SearchInfo.SalesCode':'',
            'revAvailabilitySearch.SearchInfo.SearchStations[0].DepartureStationCode':FromCountry,
            'revAvailabilitySearch.SearchInfo.SearchStations[0].ArrivalStationCode':ToCountry,
            'revAvailabilitySearch.SearchInfo.SearchStations[0].DepartureDate':DepartureDate,
            'revAvailabilitySearch.SearchInfo.SearchStations[1].DepartureStationCode':ToCountry,
            'revAvailabilitySearch.SearchInfo.SearchStations[1].ArrivalStationCode':FromCountry,
            'revAvailabilitySearch.SearchInfo.SearchStations[1].DepartureDate':BackDate,
        }
        
        rs = requests.session()
        res1 = rs.post("http://makeabooking.flyscoot.com/Book/?culture=zh-tw", data = payload)
        time.sleep(3)
        res2 = rs.get("http://makeabooking.flyscoot.com/Book/Flight")
        
        bsObj = bs(res2.text,"lxml")
        info = bsObj.findAll("div",{"class":"tab-area"})
        
        if(len(info) == 0):
            print('?'*20) 
            print('your input is wrong, please reinput') 
            break
        else:
            print('\n'+'-'*40)
            print("Get Departure time: ", DepartureDate)
            print("Get Back time: ",BackDate)
            print("data processing ... ... please wait")
            
            #departure
            depart = info[0].findAll("span")
            depart_list = [departitem.get_text().split() for departitem in depart]
            
            #back
            back = info[1].findAll("span")
            back_list = [backitem.get_text().split() for backitem in back]
            
            # departure time process
            for departitem in depart_list:
                price = "".join(list(filter(str.isdigit, departitem[3])))
                if(price!=''):
                    price = int(price)
                    depart_key = departitem[0].strip(',')+'/'+departitem[1]+'/'+departitem[2]
                    depart_dict[depart_key] = price
            depart_dict_order = collections.OrderedDict(sorted(depart_dict.items(), key=itemgetter(1), reverse=False))
             
            # back time process
            for backitem in back_list:
                price = "".join(list(filter(str.isdigit, backitem[3])))
                if(price!=''):
                    price = int(price)
                    back_key = backitem[0].strip(',')+'/'+backitem[1]+'/'+backitem[2]
                    back_dict[back_key] = price
            back_dict_order = collections.OrderedDict(sorted(back_dict.items(), key=itemgetter(1), reverse=False))
            
            # shift date
            Departure_obj += datetime.timedelta(days = 12)
            BackDate_obj += datetime.timedelta(days = 12)
            time.sleep(3)
      
    if(len(info) != 0):
        print(" process done "+'-'*40)
        
        print("\ndepart time price is : \n")
        for k, v in depart_dict_order.items():
            print(k, v)
            
        print('-'*40)
        
        print("\nback time price is : \n")
        for k, v in back_dict_order.items():
            print(k, v)
            
        break
    
#os.system("pause")