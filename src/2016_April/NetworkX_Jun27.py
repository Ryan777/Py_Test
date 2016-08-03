#encoding=utf8
### 这个已经实现了目的. 只差一个输出layout的选择. 并且, 如果是没关注原推以及所有其他比他先RT的人, 还没有把它连进原推.计划之后用不同的颜色来表示

import networkx as nx
import matplotlib.pyplot as plt

from networkx_viewer import Viewer
import tweepy
from local_config import *

import mysql.connector
import time
## initialization
conn = mysql.connector.connect(user='root', password='777',
                              host='127.0.0.1',
                              database='Proposal',
                              charset = 'utf8mb4')
# change charset to utf8mb4
c = conn.cursor()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,  wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

Tweet_DB = ''
Fellowship_DB = ''
original_user = 182695900


##要做好排序
c.execute("SELECT User_id FROM `To_be_analyzed` ORDER BY Local_Time;")
retweeter_ids_temp = c.fetchall()
all_retweeters = []
for user in retweeter_ids_temp:
    all_retweeters.append(int(user[0]))  ## int
print "There are "+ str(len(all_retweeters))+" retweeters in total!"
print "The very first retweeter is "+str(all_retweeters[0])+", second : "+ str(all_retweeters[1])

unfound_users = set(all_retweeters)
all_retweeters.insert(0, original_user)

##  MultiDiGraph??? Maybe for fellowship.
G= nx.DiGraph()


def get_followers(userID):
    ## get user's followers
    c.execute("SELECT Follower_ID FROM `Fellowship_Jun_Cleaned` where User_ID = "+ str(userID))  ### why do I need to str(userID), i think it is a string already
    followers_id_tmp = c.fetchall()
    followers = []
    for follower in followers_id_tmp:
        followers.append(int(follower[0]))    ### make it a list of int
    print "There are "+ str(len(followers))+" followers of "+str(userID)+" !"
    followers = set(followers)  ## convert it to a set
    # print len(followers)
    return followers


imported_number = 0
for user in all_retweeters:
    if user not in G:
        G.add_node(user)
    followers = get_followers(user)
    to_be_connected = followers & unfound_users
    for i in to_be_connected:
        ### add_edge() will add nodes automatically if it is not already in the graph
        # if i not in G:
        #     G.add_node(i)
        G.add_edge(i,user)
    unfound_users = unfound_users - followers ## followers or to_be_connected ?? which one is better
    if user in unfound_users:
        unfound_users.remove(user)  ### remove user itself if it is still not found
        G.add_edge(user,original_user)
        ### in this case, means this user is not be connected to his parent, so just connect it to the original one (he probably got the tweet by searching function)
    imported_number +=1
    print "Already imported "+str(imported_number)+" users."
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

# 会覆盖源文件, 很危险!
file_name = "Graph_"+time.strftime("%Y-%m-%d-%H%M", time.localtime())
nx.write_graphml(G,path = '/Users/Rampage/movies/'+file_name+'.graphml')
nx.write_graphml(G,path = '/Users/Rampage/movies/'+file_name+'_backup.graphml')  ## get a back-up
#
# # followers = get_followers('55261782')
# # print followers
# # print all_retweeters
# # print unfound_users & followers