'''
Created on Jan 5, 2559 BE

@author: Rampage
'''
import json
import pandas as pd
import matplotlib as plt

from tweepy.streaming import StreamListener
from local_config import *
from tweepy import Stream
import tweepy


class StdOutListener(StreamListener):
    
    def on_data(self, data):
        print data
        return True
    def on_error(self, status):
        return status


if __name__ ==  '__main__':
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    l = StdOutListener()
    stream = Stream(auth,l)
    
    stream.filter(track=['songkran'], languages=['th'], encoding='utf-8')
    
