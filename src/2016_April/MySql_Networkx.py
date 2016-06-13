### Get the retweeter names from a specific tweet, but it seems not complete,
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

c.execute("SELECT User_id FROM `Paul Ryan` where Original_id = '738567224600858625' ORDER BY Local_Time;")
retweeter_ids_temp = c.fetchall()
all_retweeters = []
for user in retweeter_ids_temp:
    all_retweeters.append(int(user[0]))
print "There are "+ str(len(all_retweeters))+" retweeters in total!"



unfound_users = set(all_retweeters)

original_user = "249346453"
all_retweeters.insert(0, original_user)


G= nx.DiGraph()


def get_followers(userID):
    ## get user's followers
    c.execute("SELECT Follower_ID FROM `Fellowship` where User_ID = "+ str(userID))  ### why do I need to str(userID), i think it is a string already
    followers_id_tmp = c.fetchall()
    followers = []
    for follower in followers_id_tmp:
        followers.append(int(follower[0]))
    print "There are "+ str(len(followers))+" followers of "+str(userID)+" !"
    followers = set(followers)
    print len(followers)
    return followers


for user in all_retweeters:
    if user not in G:
        G.add_node(user)
    followers = get_followers(user)
    to_be_connected = followers & unfound_users
    for i in to_be_connected:
        if i not in G:
            G.add_node(i)
        G.add_edge(i,user)
    unfound_users = unfound_users - followers
    if user in unfound_users:
        unfound_users.remove(user)  ### remove user itself if it is still not found
    if not unfound_users:
        break

if unfound_users:
    for i in unfound_users:
        G.add_edge(i,original_user)

app = Viewer(G)
app.mainloop()

#
# nx.draw(G,with_labels=False)
# plt.show()
