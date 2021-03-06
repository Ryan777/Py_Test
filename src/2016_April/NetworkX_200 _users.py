#encoding=utf8
### 这个已经实现了目的. 只差一个输出layout的选择. 并且, 如果是没关注原推以及所有其他比他先RT的人, 还没有把它连进原推.计划之后用不同的颜色来表示

import networkx as nx
import matplotlib.pyplot as plt

from networkx_viewer import Viewer
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
api = tweepy.API(auth,  wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


##要做好排序
c.execute("SELECT User_id FROM `Paul Ryan` where Original_id = '738567224600858625' ORDER BY Local_Time;")
retweeter_ids_temp = c.fetchall()
all_retweeters = []
for user in retweeter_ids_temp:
    all_retweeters.append(int(user[0]))
print "There are "+ str(len(all_retweeters))+" retweeters in total!"

unfound_users = set(all_retweeters)

original_user = 249346453
all_retweeters.insert(0, original_user)


G= nx.DiGraph()


def get_followers(userID):
    ## get user's followers
    c.execute("SELECT Follower_ID FROM `Fellowship` where User_ID = "+ str(userID))  ### why do I need to str(userID), i think it is a string already
    followers_id_tmp = c.fetchall()
    followers = []
    for follower in followers_id_tmp:
        followers.append(int(follower[0]))    ### make it a list of int
    print "There are "+ str(len(followers))+" followers of "+str(userID)+" !"
    followers = set(followers)  ## convert it to a set
    print len(followers)
    return followers


### add_edge() will add nodes automatically if it is not already in the graph
for user in all_retweeters:
    if user not in G:
        G.add_node(user)
    followers = get_followers(user)
    to_be_connected = followers & unfound_users
    for i in to_be_connected:
        if i not in G:
            G.add_node(i)
        G.add_edge(i,user)
    unfound_users = unfound_users - followers ## followers or to_be_connected ?? which one is better
    if user in unfound_users:
        unfound_users.remove(user)  ### remove user itself if it is still not found
        G.add_edge(user,original_user)
        ### in this case, means this user is not be connected to his parent, so just connect it to the original one (he probably got the tweet by searching function)
    if not unfound_users:
        break
#
# ### to be modified
# if unfound_users:
#     print unfound_users
#     for i in unfound_users:
#         G.add_edge(i,original_user)
#
# # app = Viewer(G)
# # app.mainloop()
#
# #
# # nx.draw(G,with_labels=True)
# # plt.show()
#
nx.write_graphml(G,path = '/Users/Rampage/movies/MattOswaltVA.graphml')
nx.write_graphml(G,path = '/Users/Rampage/movies/MattOswaltVA_original.graphml')  ## get a back-up
#
# # followers = get_followers('55261782')
# # print followers
# # print all_retweeters
# # print unfound_users & followers