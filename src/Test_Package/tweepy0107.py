'''
Created on Jan 7, 2559 BE

@author: Rampage
'''
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from local_config import *



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):
    def on_data(self,data):
        try:
            with open('python.json','a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on data : %s" %str(e))
        return True
    def on_error(self, status):
        print(status)
        return True
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['Star wars'])
#             
#             
# class MyListener(StreamListener):
#  
#     def on_data(self, data):
#         try:
#             with open('python.json', 'a') as f:
#                 f.write(data)
#                 return True
#         except BaseException as e:
#             print("Error on_data: %s" % str(e))
#         return True
#  
#     def on_error(self, status):
#         print(status)
#         return True
#  
# twitter_stream = Stream(auth, MyListener())
# twitter_stream.filter(track=['#python'])