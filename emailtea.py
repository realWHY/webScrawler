from catchPTTtitle_raw import getPTTInfo
import weatherscrawler as ws
import win32com.client as win32
import random

##to_list = ["Hungyu.Wei@abilitycorp.com.tw"]
to_list = ["Tim.Lee@abilitycorp.com.tw",
           "Panda.Wang@abilitycorp.com.tw",
           "Hungyu.Wei@abilitycorp.com.tw",
           "YenLin.Chen@abilitycorp.com.tw",
           "Levis.Cheng@abilitycorp.com.tw",
           "Michael.Shih@abilitycorp.com.tw",
           "Jw.Wang@abilitycorp.com.tw",
           "Ian.Huang@abilitycorp.com.tw",
           "Liam.Hsieh@abilitycorp.com.tw",
           "Allen.Yang@Abilitycorp.com.tw",
           "Richard.Liu@abilitycorp.com.tw",
           "Lewis.Tsai@abilitycorp.com.tw"]

city = 'New_Taipei_City'
weatherLinkUrl = 'http://www.cwb.gov.tw/V7/forecast/taiwan/'+ city +'.htm'
##pttLinkUrl = 'https://www.ptt.cc/bbs/Beauty/index.html'
##pttLinkUrl ="https://www.ptt.cc/bbs/Tech_Job/index2593.html"
whichWeather = '讓我們來關心天氣 ^.< \n\n'

#define ptt key
ptt_jobKey = "https://www.ptt.cc/bbs/Tech_Job/index.html"
ptt_beautyKey = "https://www.ptt.cc/bbs/Beauty/index.html"
ptt_stupidKey = "https://www.ptt.cc/bbs/StupidClown/index.html"
ptt_boygirlKey = "https://www.ptt.cc/bbs/Boy-Girl/index.html"
#ptt_jokeKey = "https://www.ptt.cc/bbs/joke/index.html"
ptt_movieKey = "https://www.ptt.cc/bbs/movie/index.html"
ptt_muscleKey = "https://www.ptt.cc/bbs/MuscleBeach/index.html"
#ptt_lifemoneyKey = "https://www.ptt.cc/bbs/Lifeismoney/index.html"
ptt_bktballKey = "https://www.ptt.cc/bbs/NBA/index.html"
ptt_aviationKey = "https://www.ptt.cc/bbs/Aviation/index.html"
#ptt_buytoKey = "https://www.ptt.cc/bbs/BuyTogether/index.html"
ptt_StockKey = "https://www.ptt.cc/bbs/Stock/index.html"
ptt_overSeaJobKey = "https://www.ptt.cc/bbs/oversea_job/index.html"

#ptt list
ptt_list = [ptt_jobKey, ptt_beautyKey, ptt_boygirlKey, ptt_stupidKey, ptt_movieKey,
            ptt_muscleKey, ptt_bktballKey, ptt_aviationKey,
            ptt_StockKey, ptt_overSeaJobKey]

##ptt_random_num = random.randint(0,len(ptt_list)-1)
with open('C:\emailSend\count.txt', 'r', encoding='UTF-8') as file:
    for num in file:
        ptt_circle_num = int(num)
        ptt_circle_num %= len(ptt_list)

ptt_key = ptt_list[ptt_circle_num]

ptt_circle_num +=1
ptt_circle_num = str(ptt_circle_num)
with open('C:\emailSend\count.txt', 'w', encoding='UTF-8') as file:
    file.write(ptt_circle_num)
    
#ptt url
ptt_url = {ptt_jobKey: 'Job版 最新最Cool !!!! \n',
           ptt_beautyKey : 'Beauty版 最新最Hot !!!! \n',
           ptt_stupidKey : '笨版 最新最笨 !!!! \n',
           ptt_boygirlKey: '男女版 最新最狗男女! \n',
           #ptt_jokeKey : 'joke版 : 好像很好笑!! \n',
           ptt_movieKey : 'Movie版: 最Hot電影 \n',
           ptt_muscleKey : '健身版: 阿斯來健身\n',
           #ptt_lifemoneyKey : '省錢版 : 省錢就像白T牛仔褲，永不退流行。\n',
           ptt_bktballKey : 'NBA版 : Three point shot !!!\n',
           ptt_aviationKey : '航空版 : 你搞甚麼飛機!\n',
           #ptt_buytoKey : '一起買版 : 讓我們一起月光吧!! money buybuy\n',
           ptt_StockKey : 'Stock 版: 只要你有錢 人人都是股神!!\n',
           ptt_overSeaJobKey : 'OverseaJob版 : 塊陶!!!\n'}
            
pttLinkUrl = ptt_key
whichPtt = ptt_url[ptt_key]

#remove or add what user dislike

if(ptt_key != ptt_beautyKey):
    if "Ian.Huang@abilitycorp.com.tw" in to_list:
        to_list.remove("Ian.Huang@abilitycorp.com.tw")
    
# weather report
weatherContent = ws.getLinks(weatherLinkUrl)
pttContent = whichPtt + getPTTInfo(pttLinkUrl)

'''
prog_recom = ('好片推薦 : 世紀天才\n'+'預告 :\n'+
            'https://www.youtube.com/watch?v=VsJDjv_rMmo'+
            '\n正片: \n'+
            'https://www.youtube.com/watch?v=2JEa4mLY4Pk'+'\n')
'''

sepLine = '-'*50+'\n'
footer = "每天兩小時(13:30~15:30) 請持續鎖定WHY報報歐!"

for maillist in to_list:
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    print(maillist)
    mail.To = maillist
    mail.Subject = '[WHY報報] 訂便當 + 天氣預報 +'+ whichPtt
    mail.Body = ('不要忘記訂便當唷 (≖‿ゝ≖)✧ '+'\n'+ sepLine
                #+ prog_recom + sepLine
                + whichWeather + weatherContent
                + '\n' + sepLine + pttContent + sepLine + footer)
    mail.Send()


