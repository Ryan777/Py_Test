import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
import time
import json
from local_config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

status_all = api.get_status(id = 643081597156114432)
# status = json.loads(status_all)
# for result in api.search(q="football"):
#     print result.text
print status_all.user.screen_name