#encoding=utf-8
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
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

    def on_data(self, data):

        all_data = json.loads(data)
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]
        id = all_data["id_str"]

        retweeted_id = ""
        retweeted_user = ""
        retweet_count = "-1"
        # print(username)
        # print(tweet)
        if("retweeted_status" in all_data):
            retweeted_id = all_data["retweeted_status"]["id_str"]
            retweeted_user = all_data["retweeted_status"]["user"]["screen_name"]
            retweet_count = all_data["retweeted_status"]["retweet_count"]

        followers_count = all_data["user"]["followers_count"]

        # print(mentioned_user )

        # print("--------------------")


        tTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(all_data["timestamp_ms"]) / 1000.0))

        # c.execute("INSERT INTO  (ID, User_name, Retweeted_user, time, tweet, followers_count) VALUES (%s,%s,%s,%s,%s,%s)",
        #     (id, username, retweeted_user, tTime, tweet,followers_count ))

        # c.execute("INSERT INTO โคตรตอแหล (ID, User_name, Retweeted_id, Retweeted_user,, retweeted_count, time, tweet, followers_count) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        #     (id, username, retweeted_id, retweeted_user, tTime, tweet,followers_count ))
        ### Have to COMMIT !!!!!

        # c.execute("INSERT INTO `"+ myTopic +"` (ID, User_name, Retweeted_id, Retweeted_user, Retweeted_count, Local_time, tweet, followers_count) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        #     (id, username, retweeted_id, retweeted_user, retweet_count, tTime, tweet,followers_count ))
        # conn.commit()

        print(id)
        # print(tweet)
        # print(tTime)
        print(data)

        print("--------------------")
        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

#input the keyword here and it will be filtered from Twitter and written to the database
# There are some problems with Thai encoding !!!!!!!!!!!!!!!!
myTopic ="I'm in Bangkok"
twitterStream = Stream(auth, listener())
twitterStream.filter(track=[myTopic])
