#coding=utf-8
import requests
from bs4 import BeautifulSoup
import re


url = 'http://www.heibanke.com/lesson/crawler_ex00/72324/'
def spider(myNext):
    while True:
        url = 'http://www.heibanke.com/lesson/crawler_ex00/'+myNext+'/'
        myRequests = requests.get(url)
        plain_text = myRequests.text

        soup = BeautifulSoup(plain_text, "html.parser")

        for line in soup.find_all('h3'):
            print line.string
            myNext = re.findall(r'\d+',line.string)[0]
            if myNext == None:
                break
spider('72324')