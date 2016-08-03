#encoding=utf-8
### Basic Streaming, the Listener is a little bit different from previous one.
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from local_config import *
# import mysql.connector
import time
import json

#
# conn = mysql.connector.connect(user='root', password='777',
#                               host='127.0.0.1',
#                               database='Twitter',
#                               charset = 'utf8mb4')
# # change charset to utf8mb4
# c = conn.cursor()


ckey='7FWpTHkeQMaO1bnHQYnd62De8'
csecret='albUzEWdlrpI9gP8uH7FcCHi1Cgo2QLeKSPLPqNVIAUMimM2Fa'
atoken='2668995974-UKVj9CIcCF0zfIeCBRvIyOGqL1oPPi6OJ1fH1y6'
asecret='g7TgKKOJ0Bj1ua7UvGnWT98ztvmzVXA72OIcd04OCifZU'

class listener(StreamListener):

    def on_status(self, status):
        print status.text     ## it is the same as "all_data" in another version
        return True
    # def on_data(self, data):
    #     all_data = json.loads(data)
    #     print all_data
    #     tweet = all_data["text"]
    #     print "-------------"

    def on_error(self, status_code):
        print(status_code)
        print "here is an error"
        return True

    def on_timeout(self):
        print "Timeout"
        return True


if __name__ == '__main__':

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth,  wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

    #input the keyword here and it will be filtered from Twitter and written to the database
    # There are some problems with Thai encoding !!!!!!!!!!!!!!!!
    myTopic ="I'm in Bangkok"
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track = ['#FathersDay'])
