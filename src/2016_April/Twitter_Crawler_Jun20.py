#coding=utf-8
#coding=utf-8
#encoding=utf-8
import traceback
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from local_config import *
import mysql.connector
import time
import json

# change charset to utf8mb4
conn = mysql.connector.connect(user='root', password='777',
                              host='127.0.0.1',
                              database='Proposal',
                              charset = 'utf8mb4')
c = conn.cursor()


class listener(StreamListener):

    def on_data(self, data):

        all_data = json.loads(data)
        # tweet = all_data["text"]
        # print tweet
        username = ""
        user_id = ""
        id = ""
        followers_count = "0"
        tweet = ""

        if("user" in all_data):
            tweet = all_data["text"]
            # print tweet
            username = all_data["user"]["screen_name"]
            user_id = all_data["user"]["id"]
            id = all_data["id_str"]
            ## follower_count of the retweeter
            followers_count = all_data["user"]["followers_count"]


        original_id = ""
        original_user = ""
        retweet_count = "0"
        original_followers = "0"

        if("retweeted_status" in all_data):
            original_id = all_data["retweeted_status"]["id_str"]
            original_user = all_data["retweeted_status"]["user"]["screen_name"]
            retweet_count = all_data["retweeted_status"]["retweet_count"]
            original_followers = all_data["retweeted_status"]["user"]["followers_count"]

        # print data
        # print(mentioned_user )

        # print("--------------------")
        tTime = "0"
        if "timestamp_ms" in all_data:
            tTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(all_data["timestamp_ms"]) / 1000.0))
        ### Have to COMMIT !!!!!

        c.execute("INSERT IGNORE INTO `"+ table_name +"` (ID, User_name, User_id, Followers_count, Retweet_count, Original_user, Original_id, Original_followers, Tweet, Local_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                  (id, username, user_id, followers_count, retweet_count, original_user, original_id, original_followers, tweet, tTime))
        #### added IGNORE ####
        conn.commit()
        print tTime


        return True

    def on_error(self, status_code):
        print(status_code)

        return True

    def on_timeout(self):
        print "Timeout"
        return True

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#input the keyword here and it will be filtered from Twitter and written to the database
# There are some problems with Thai encoding !!!!!!!!!!!!!!!!
### HAVE TO MODIFY HERE ABOUT "AUTO EXIT"         "Process finished with exit code 0" if it catches a KeyError

keywords = ['Zhou Qi']
table_name ="Zhou Qi"
#### added PRIMARY KEY ####
c.execute("create table if not exists `"+ table_name +"` (ID VARCHAR(23), User_name VARCHAR(40) Character set utf8mb4, User_id VARCHAR(23), Followers_count INT(11), Retweet_count INT(11), Original_user VARCHAR(40) Character set utf8mb4, Original_id VARCHAR(23),  Original_followers INT(11), Tweet VARCHAR(255) Character set utf8mb4, Local_time VARCHAR(22),   PRIMARY KEY (ID))")



# print "Start streaming "+ str(keywords) +" ...."
twitterStream = Stream(auth, listener())
# twitterStream.filter(track=keywords)

## locations -- west, south, east, north
print "Start streaming ZhouQi"
# twitterStream.filter(locations=[-97.34,5.61,-105.63,20.46])
twitterStream.filter(track=keywords)