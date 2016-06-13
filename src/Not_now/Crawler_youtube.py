#encoding=utf-8
#https://www.youtube.com/watch?v=pLHejmLB16o

import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 2
    while page <= max_pages:
        url = 'http://www.avxfree.com/latest-updates/'+str(page)+'/'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")
        for link in soup.findAll('a',{'rel': "nofollow"}):
            title = link.string
            href = link.get('href')
            print(href)
            print(title)
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")




trade_spider(2)
