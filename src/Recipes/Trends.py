import os
import sys
import datetime
import time
import json
from local_config import *
import tweepy


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

### write data to a disk file
if not os.path.isdir('out/trends_data'):
    os.makedirs('out/trends_data')

while True:

    now = str(datetime.datetime.now())

    trends = json.dumps(api.trends_place(23424960))

    f = open(os.path.join(os.getcwd(),'out','trends_data',now),'w')
    f.write(trends)
    f.close()

    print >> sys.stderr, "Wrote data file", f.name
    print >> sys.stderr, "Zzzz...."

    time.sleep(60)

### write data to a disk file