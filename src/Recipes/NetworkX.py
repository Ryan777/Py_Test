import sys
import json
import networkx as nx
import tweepy
from local_config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import mysql.connector
import time
import json


conn = mysql.connector.connect(user='root', password='777',
                              host='127.0.0.1',
                              database='Twitter',
                              charset = 'utf8mb4')
# change charset to utf8mb4
c = conn.cursor()


ckey='7FWpTHkeQMaO1bnHQYnd62De8'
csecret='albUzEWdlrpI9gP8uH7FcCHi1Cgo2QLeKSPLPqNVIAUMimM2Fa'
atoken='2668995974-UKVj9CIcCF0zfIeCBRvIyOGqL1oPPi6OJ1fH1y6'
asecret='g7TgKKOJ0Bj1ua7UvGnWT98ztvmzVXA72OIcd04OCifZU'

class listener(StreamListener):

    def on_data(self, data):

        all_data = json.loads(data)
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]
        id = all_data["id_str"]

        retweeted_user = ""
        if("retweeted_status" in all_data):
            retweeted_user = all_data["retweeted_status"]["user"]["screen_name"]
        if retweeted_user != "":



        tTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(all_data["timestamp_ms"]) / 1000.0))



        print(id)
        print(tweet)


        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

#input the keyword here and it will be filtered from Twitter and written to the database
topic ="Test"
twitterStream = Stream(auth, listener())
twitterStream.filter(track=[topic])
