#! usr/bin/python
import pyttsx
import speech_recognition as sr 
from bs4 import BeautifulSoup
import mechanize
from mechanize._opener import urlopen
import pyaudio
import os
import pytz, time
from datetime import datetime

engine=pyttsx.init()


#Mechanize a browser and get the html from the url
#Then return the html
def mech(url):
    br=mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    cookies=mechanize.CookieJar()
    br.set_cookiejar(cookies)
    br.addheaders=[('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/543.7 (KTML, like Gecko) Chrome/7.0.517.41 Safari/543.7')]
    response=br.open(url)
    return(response.read())

def date():
    now=datetime.now()
    month='none'
    #month=time.strftime("%B") This doesnt work, why!?!?!?!?!

    if now.month == 1:
        month='January'
        return('The date is', str(month), str(now.day), str(now.year))
    elif now.month == 2:
        return('The date is', str(month), str(now.day), str(now.year))
        month='February'
        return('The date is', str(month), str(now.day), str(now.year))
    elif now.month == 3:
        month='March'
        return('The date is', str(month), str(now.day), str(now.year))
    elif now.month == 4:
        month='April'
        return('The date is', str(month), str(now.day), str(now.year))
    elif now.month == 5:
        month='May'
        return('The date is', str(month), str(now.day), str(now.year))
    elif now.month == 6:
        month='June'
        return('The date is', str(month), str(now.day), str(now.year))
    elif now.month == 7:
        month='July'
        return('The date is', str(month), str(now.day), str(now.year))
    elif now.month == 8:
        month='August'
        return('The date is', str(month), str(now.day), str(now.year))
    elif now.month == 9:
        month='September'
        return('The date is', str(month), str(now.day), str(now.year))
    elif now.month == 10:
        month='October'
        return('The date is', str(month), str(now.day), str(now.year))
    elif now.month == 11:
        month='November'
        return('The date is', str(month), str(now.day), str(now.year))
    elif now.month == 12:
        month='December'
        return('The date is', str(month), str(now.day), str(now.year)) 
    return('The date is', str(month), str(now.day), str(now.year))

def time():
    now=datetime.now()
    if now.hour>12:
      hour=now.hour-12
    else:
      hour=now.hour
    return('The time is', str(hour), str(now.minute))


#Pass mechanize the weather website
#Vocalize the results as parsed by beautiful soup
def weather():
    url='http://doineedanumbrella.com/?q=32816'
    content=mech(url)
    soup = BeautifulSoup(content)

    rain=soup.find_all("p", {"class": "phrase"})
    temp=soup.find_all("p", {"class": "status"})

    for item in temp:
        print item.text
        engine.say(item.text)    

    for item in rain:
        print item.text
        engine.say(item.text) 

#Listen for phrases
#Phrases said go into test
#Test then runs in a for loop that determines the response
#The response is based on what test heard 
def switch(test):
        
    print test
    if all(x in test for x in ["Hello there"]):
        engine.say("Hello there")

    elif test=="Jarvis":
        engine.say("Listening Sir")
        engine.runAndWait()
        engine.say(" ")
        engine.runAndWait()

    elif all(x in test for x in ['time']):
        engine.say(time())

    elif all(x in test for x in ['weather']):
        weather()

    elif all(x in test for x in ['date']):
        engine.say(date()) 

    elif all(x in test for x in ['today', 'like']):
        engine.say(time())
        engine.say(date())
        weather()
        #engine.runAndWait()
      
    return(test)
