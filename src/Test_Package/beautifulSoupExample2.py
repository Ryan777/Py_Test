'''
Coursera Python ---- Link see below
https://pr4e.dr-chuck.com/tsugi/mod/python-data/index.php?PHPSESSID=47e9ea09ed1635242cfdcf82a97ad33d

Created on Jan 15, 2559 BE

@author: Rampage
'''
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

for i in range(7):
    html = urllib.urlopen(url).read()
    soup = BeautifulSOAP(html)
    
    tags = soup('a')

    list = []
    for tag in tags:
        list.append(tag.get('href',None))
        ### tag.contents[0] ---- get the string text (aka the "name") on the link
    print list[17]
    
    url = list[17]
