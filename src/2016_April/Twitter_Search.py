import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
import time
import json
from local_config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search,
                           q="google",
                           rpp=100,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items():
    print tweet.created_at, tweet.text