#coding=utf-8
import tweepy
from local_config import *

# Replace the API_KEY and API_SECRET with your application's key and secret.  ( consumer_key & consumer_secret )
# auth = tweepy.AppAuthHandler('consumer_key', 'consumer_secret')
# api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,  wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

# api.update_status("test")
