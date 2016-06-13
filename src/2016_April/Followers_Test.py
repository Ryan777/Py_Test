#coding=utf-8
#### import all the followers of a user to the Fellowship database

import tweepy
from local_config import *

import mysql.connector
conn = mysql.connector.connect(user='root', password='777',
                              host='127.0.0.1',
                              database='Proposal',
                              charset = 'utf8mb4')
# change charset to utf8mb4
c = conn.cursor()



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

i = 0
# followers = api.followers_ids(id='alexandraizqRD')
original_id = '55261782'
followers_id =[]

for page in tweepy.Cursor(api.followers_ids, id=original_id).pages():
    followers_id.extend(page)
    # print type(page)
    # print page
    # print "-----"
    print len(followers_id)
    # print followers_id

for aFollower in followers_id:
    c.execute("INSERT INTO `Fellowship` (User_ID, Follower_id) VALUES (%s,%s)",(original_id, aFollower))
conn.commit()

# c.execute("INSERT INTO Followers_network (ID, Followers_id) VALUES (%s,%s)",(original_id, followers_id))

# print followers
#
# print len(followers)
