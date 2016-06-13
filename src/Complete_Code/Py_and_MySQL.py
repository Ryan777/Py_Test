from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import mysql.connector
import time
import json


conn = mysql.connector.connect(user='root', password='777',
                              host='127.0.0.1',
                              database='tweepy',
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
        
        c.execute("INSERT INTO test_table1 (time, username, tweet) VALUES (%s,%s,%s)",
            (time.time(), username, tweet))

        conn.commit()

        print((username,tweet))
    
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Star wars"]) 
    