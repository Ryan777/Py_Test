'''
From the video but there is bug

Created on Feb 2, 2559 BE

@author: Rampage
'''
import json
import urllib
from astropy.wcs.docstrings import lng

# ''
serviceurl = "http://map.googleapis.com/maps/api/geocode/json?"

while True:
    address = raw_input("Enter your address : ")
    if len(address) < 1: break
    
    url = serviceurl + urllib.urlencode({'sensor':'false' , 'address' : address})

    print "Retrieving", url
    
    uh = urllib.urlopen(url)
    data = uh.read()
    print "Retrieved ",len(data)," characters"
    
    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != "OK":
        print "=======Failed to retieve========"
        print data
        continue
    
    print json.dumps(js, indent=4) 
    
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print "lat",lat,'lng',lng
    location = js['results'][0]['formatted_address']
    
    print location