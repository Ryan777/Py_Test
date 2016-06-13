#coding=utf-8
import requests
from bs4 import BeautifulSoup

def bd_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://tieba.baidu.com/p/3157910883?pn="+str(page)
        # url ="http://tieba.baidu.com/f?kw=%E7%AC%91%E8%AF%9D&ie=utf-8&tp=0"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for line in soup.find_all('div',{'class':'d_post_content j_d_post_content '}):
            text = line.string
            print text

        page += 1

bd_spider(1)