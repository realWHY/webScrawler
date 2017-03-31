from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime as dt
import os

city = 'New_Taipei_City'
linkUrl = 'http://www.cwb.gov.tw/V7/forecast/taiwan/'+ city +'.htm'

def getLinks(pageUrl):
    html = urlopen(pageUrl)
    bsObj = BeautifulSoup(html)
    curHour = getCurHour()
    
    #info = bsObj.findAll("th",{"scope":"row"})
    info = bsObj.findAll("tr")
    predict1 = info[1].get_text().strip().split()
    predict2 = info[2].get_text().strip().split()
    predict3 = info[3].get_text().strip().split()

    
    print('predict1 = ',predict1)
    print('predict2 = ',predict2)
    print('predict3 = ',predict3)
    
    
    
    weatherReport1 = (predict1[0]+" => "+predict1[7]+",降雨機率為"+predict1[8]+
                    predict1[9])
    print('weatherReport1 = ',weatherReport1)

    weatherReport2 = (predict2[0]+" => "+predict2[7]+",降雨機率為"+predict2[8]+
                    predict2[9])
    print('weatherReport2 = ',weatherReport2)

    weatherReport3 = (predict3[0]+" => "+predict3[7]+",降雨機率為"+predict3[8]+
                    predict3[9])
    print('weatherReport3 = ',weatherReport3)
    

    weatherString = weatherReport1+'\n'+weatherReport2+'\n'+weatherReport1+'\n'
    #print('weatherString = ',weatherString)
    
    if(predict1[1] == predict2[1] and curHour<23):
        wea_today = ""
        
        tempS = predict1[7]+","
        if(int(predict1[8])>50 and int(predict2[8])<50):
            wea_today = "今天"+tempS+"白天有很高降雨機率, 請記得攜帶雨具"
        elif(int(predict1[8])<30 and int(predict2[8])<30):
            wea_today = "今天"+tempS+"降雨機率非常低, 享受好天氣吧"
        elif(int(predict1[8])<50 and int(predict2[8])>50):
            wea_today = "今天"+tempS+"晚上有很高降雨機率, 請記得攜帶雨具"
        else:
            wea_today = "今天"+tempS+"有較小降雨機率, 還算是不錯的天氣"
        print(wea_today)
    else:
        wea_today = ""
        wea_tomorrow = ""
        if(curHour<23):
            tempS = predict1[7]+","
            if(int(predict1[8])>50):
                wea_today = "今天晚上"+tempS+"有很高降雨機率, 請記得攜帶雨具"
            elif(int(predict1[8])<30):
                wea_today = "今天晚上"+tempS+"降雨機率非常低, 好好享受夜晚吧"
            else:
                wea_today = "今天晚上"+tempS+"有較小降雨機率, 還算是不錯的天氣"
            print(wea_today)   
        
        if(curHour>20):
            tempS_t = predict2[7]+","
            if(int(predict2[8])>50 and int(predict3[8])<50):
                wea_tomorrow = "明天"+tempS_t+"白天有很高降雨機率, 請記得攜帶雨具"
            elif(int(predict2[8])<30 and int(predict3[8])<30):
                wea_tomorrow = "明天"+tempS_t+"降雨機率非常低, 享受好天氣吧"
            elif(int(predict2[8])<50 and int(predict3[8])>50):
                wea_tomorrow = "明天"+tempS_t+"晚上有很高降雨機率, 請記得攜帶雨具"
            else:
                wea_tomorrow = "明天"+tempS_t+"降雨機率不高, 還算是不錯的天氣呢"
            print(wea_tomorrow)

    return weatherString

    '''
    print('predict1 = ',predict1)
    print('predict2 = ',predict2)
    print('predict3 = ',predict3)

    if(curHour>0 and curHour<12):
        print('section1')
    elif(curHour>12 and curHour<18):
        print('section2')
    elif(curHour>18 and curHour<18):
        print('section2')

    
    print('daytime_weather = ',daytime_weather)
    print('tonight_weather = ',tonight_weather)
    print('tomorrow_weather = ',tomorrow_weather)
    '''

def getCurHour():
    return dt.datetime.now().hour
    
if __name__ == "__main__":
    weatherString = getLinks(linkUrl)
    print('weatherString = ',weatherString)
    os.system("pause")
    
