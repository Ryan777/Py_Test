#coding=utf-8
#encoding=utf-8
import traceback
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import mysql.connector
import time
import json


conn = mysql.connector.connect(user='root', password='777',
                              host='127.0.0.1',
                              database='Proposal',
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
        # tweet = all_data["text"]
        # print tweet
        username = ""
        user_id = ""
        id = ""
        followers_count = "0"

        if("user" in all_data):
            # tweet = all_data["text"]
            username = all_data["user"]["screen_name"]
            user_id = all_data["user"]["id"]
            id = all_data["id_str"]
            ## follower_count of the retweeter
            followers_count = all_data["user"]["followers_count"]


        Original_id = ""
        Original_user = ""
        retweet_count = "0"
        followers_count_original = "0"

        if("retweeted_status" in all_data):
            Original_id = all_data["retweeted_status"]["id_str"]
            Original_user = all_data["retweeted_status"]["user"]["screen_name"]
            retweet_count = all_data["retweeted_status"]["retweet_count"]
            followers_count_original = all_data["retweeted_status"]["user"]["followers_count"]


        # print(mentioned_user )

        # print("--------------------")
        tTime = "0"
        if "timestamp_ms" in all_data:
            tTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(all_data["timestamp_ms"]) / 1000.0))
        ### Have to COMMIT !!!!!

        # c.execute("INSERT INTO `"+ myTopic +"` (ID, User_name, User_id, Original_id, Original_user, Retweeted_count, Local_time, followers_count) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        #     (id, username, user_id, Original_id, Original_user, retweet_count, tTime, followers_count ))

        ### if there is not a same ID in the table, insert this tweet... Maybe there is a problem, it slows the database because it has to check with the every single data
        # c.execute("INSERT INTO `"+ myTopic +"` (ID, User_name, User_id, Original_id, Original_user, Retweeted_count, Local_time, followers_count, followers_count_original) SELECT %s,%s,%s,%s,%s,%s,%s,%s,%s FROM DUAL WHERE NOT EXISTS(SELECT ID FROM `"+ myTopic +"` WHERE ID = %s);",
        #           (id, username, user_id, Original_id, Original_user, retweet_count, tTime, followers_count,followers_count_original,id))
        #
        c.execute("INSERT IGNORE INTO `"+ myTopic +"` (ID, User_name, User_id, Original_id, Original_user, Retweeted_count, Local_time, followers_count, followers_count_original) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                  (id, username, user_id, Original_id, Original_user, retweet_count, tTime, followers_count, followers_count_original))
        #### added IGNORE ####
        conn.commit()

        # print(id)
        # print(tweet)
        # print(tTime)
        # print(data)

        return True

    def on_error(self, status_code):
        print(status_code)

        return True

    def on_timeout(self):
        print "Timeout"
        return True

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

#input the keyword here and it will be filtered from Twitter and written to the database
# There are some problems with Thai encoding !!!!!!!!!!!!!!!!
### HAVE TO MODIFY HERE ABOUT AUTO EXIT         "Process finished with exit code 0" if it catches a KeyError

myTopic ="Test_June20"
#### added PRIMARY KEY ####
c.execute("create table if not exists `"+ myTopic +"` (ID VARCHAR(22), User_name VARCHAR(40) Character set utf8mb4, User_id VARCHAR(22), Original_id VARCHAR(22), Original_user VARCHAR(40) Character set utf8mb4, Retweeted_count INT(11), Local_time VARCHAR(22), Followers_count INT(11), Followers_count_original INT(11), PRIMARY KEY (ID))")

#
# def start_streaming():
#     while True:
#         print "Start streaming "+myTopic +" ...."
#
#         try:
#             twitterStream = Stream(auth, listener())
#             twitterStream.filter(track=['#FathersDay','#BlackPlotTwists'])
#         except KeyError:
#             localtime = time.asctime( time.localtime(time.time()) )
#             print "Error occurs :", localtime
#             continue
#             # tweet = ""
#             # username = ""
#             # id = ""
#         except:
#             raise
#
# start_streaming()


### Tested, continue the code when catch KeyError
# print "Start streaming "+myTopic +" ...."
# while True:
#     try:
#         twitterStream = Stream(auth, listener())
#         twitterStream.filter(track=['#FathersDay','#BlackPlotTwists'])
#     except KeyError:
#         localtime = time.asctime( time.localtime(time.time()) )
#         print "Error occurs :", localtime


twitterStream = Stream(auth, listener())
twitterStream.filter(track=['#GameofThrones','#NBAFinals'])