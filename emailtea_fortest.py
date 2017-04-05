'''
import smtplib

from email.mime.text import MIMEText
host = "smtp.gmail.com"
port = 587
username = "Hungyu.Wei@abilitycorp.com.tw"
password = "/.,mn09876"
from_email = username
to_list = ["Hungyu.Wei@abilitycorp.com.tw"]
#to_list = ["e94971360@livemail.tw"]
try:
    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)
    the_msg['Subject'] = "Hello there!"
    the_msg["From"] = from_email
    #the_msg["To"]  = to_list[0]
    plain_txt = "Testing the message"
    email_conn.sendmail(from_email, to_list, plain_txt.as_string())
    email_conn.quit()
except smtplib.SMTPException:
    print("error sending message")
yyyyy")
me = "Hungyu.Wei@abilitycorp.com.tw"
you = "Hungyu.Wei@abilitycorp.com.tw"
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
'''
from catchPTTtitle_raw import getPTTInfo
import weatherscrawler as ws
import win32com.client as win32
import random

to_list = ["Hungyu.Wei@abilitycorp.com.tw"]
city = 'New_Taipei_City'
weatherLinkUrl = 'http://www.cwb.gov.tw/V7/forecast/taiwan/'+ city +'.htm'
##pttLinkUrl = 'https://www.ptt.cc/bbs/Beauty/index.html'
##pttLinkUrl ="https://www.ptt.cc/bbs/Tech_Job/index2593.html"
whichWeather = '讓我們來關心天氣 ^.< \n\n'

#define ptt key
ptt_jobKey = "https://www.ptt.cc/bbs/Tech_Job/index2593.html"
ptt_beautyKey = "https://www.ptt.cc/bbs/Beauty/index.html"

#ptt list
ptt_list = [ptt_jobKey, ptt_beautyKey]

ptt_random_num = random.randint(0,len(ptt_list)-1)
print(ptt_random_num)
ptt_key = ptt_list[ptt_random_num]
#ptt url
ptt_url = {ptt_jobKey: 'Job版 最新最Cool !!!! \n',
           ptt_beautyKey : 'Beauty版 最新最Hot !!!! \n'}

pttLinkUrl = ptt_key
whichPtt = ptt_url[ptt_key]

# weather report
weatherContent = ws.getLinks(weatherLinkUrl)
pttContent = whichPtt + getPTTInfo(pttLinkUrl)

sepLine = '-'*50+'\n'

for maillist in to_list:
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    print(maillist)
    mail.To = maillist
    mail.Subject = '訂便當 + 天氣預報 +'+ whichPtt
    mail.Body = ('趕快訂便當唷'+'\n'+ sepLine + whichWeather + weatherContent
                + '\n' + sepLine + pttContent)
    mail.Send()
