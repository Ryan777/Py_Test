#coding=utf-8
import tweepy
from local_config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,  wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user_ID = api.get_user('@rAin_Nevermore')
print user_ID