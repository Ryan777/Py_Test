#coding=utf-8
import tweepy
from local_config import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

u_screen_name = "MattOswaltVA"
user_id = api.get_user(screen_name = u_screen_name)

print user_id