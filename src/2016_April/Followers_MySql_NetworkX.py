#coding=utf-8
# ### Get the retweeter names from a specific tweet, but it seems not complete,
# like it is said 66 retweet times, but I got only 58 names
# Api : tweepy--- retweets

import tweepy
from local_config import *
from networkx_viewer import Viewer
from tweepy import Stream
from tweepy import OAuthHandler
import time
import json
import networkx as nx
import matplotlib.pyplot as plt

import mysql.connector
conn = mysql.connector.connect(user='root', password='777',
                              host='127.0.0.1',
                              database='Proposal',
                              charset = 'utf8mb4')
# change charset to utf8mb4
c = conn.cursor()

auth = tweepy.AppAuthHandler('7FWpTHkeQMaO1bnHQYnd62De8', 'albUzEWdlrpI9gP8uH7FcCHi1Cgo2QLeKSPLPqNVIAUMimM2Fa')
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

### add fields manually
original_uname = ""
original_user_id = "1598644159"

followers =[]
for page in tweepy.Cursor(api.followers_ids, id= original_user_id, count = 5000).pages():
    followers.extend(page)
print len(followers)
# print followers
print "--------------------"
# store the followers into database

for follower in followers:
    c.execute("INSERT INTO Fellowship (User_ID, Follower_ID) VALUES (%s,%s)",(original_user_id, follower))
    # c.execute("INSERT INTO Fellowship (User_ID, Follower_ID) SELECT %s, %s FROM DUAL WHERE NOT EXISTS(SELECT User_ID,Follower_ID FROM Fellowship WHERE User_ID = %s &&Follower_ID = %s);",(original_user_id,follower,original_user_id,follower))
conn.commit()

c.execute("SELECT User_id FROM `Marilyn Monroe` where Original_id = '738026602605518848';")
retweeter_ids_temp = c.fetchall()
all_retweeters = []
for user in retweeter_ids_temp:
    all_retweeters.append(int(user[0]))
print len(all_retweeters)
# print all_retweeters    ## output [u'2641512495', u'4552323814', .... ] seems to be strings
print "----------------------"


undecided_retweeters = all_retweeters

tmp = [val for val in undecided_retweeters if val in followers]
undecided_retweeters = tmp
print len(undecided_retweeters)
print undecided_retweeters