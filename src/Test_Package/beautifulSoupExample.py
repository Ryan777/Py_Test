from bs4 import BeautifulSoup
import urllib

import sys
print sys.version
print sys.version_info
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#    # Look at the parts of a tag
#    print 'TAG:',tag
#    print 'URL:',tag.get('href', None)
#    print 'Contents:',tag.contents[0]
#    print 'Attrs:',tag.attrs

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')

sum = 0
for tag in tags:
    sum += int(tag.contents[0])
print sum