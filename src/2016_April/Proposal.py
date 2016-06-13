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


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# "count" is the number of the retweets, up to 100
retweets = api.retweets(id = 363644399416119296, count =100)
i = 0
# print type(retweets)
# all_users = {}
all_users = []
for retweet in retweets:
    # user_mention = ""
    # print retweet.created_at + " From "+ retweet.user.screen_name +" to " + retweet.user_mentions.screen_name
    print retweet.created_at
    print retweet.user.screen_name ### latest comes first. 2015, 2014, 2013
    # all_users[retweet.user.screen_name]= retweet.created_at
    all_users.append(retweet.user.screen_name)
    i= i+1

all_users.reverse()
print all_users   ### output : [u'sagez9master', u'PanJ', u'f_takco', u'pawin35', u'AmiHirari', u'LINTANIA', u'maerdcha', u'ShitNigSays', u'mookcifer']
print all_users[0]  ### output : sagez9master
# print all_users


##Draw ### it was MuitiDiGraph(), but then thought DiGraph() was enough
G= nx.DiGraph()
### I should add some code to identify the orignal user's name instead of calling him 'Orignal', can I do it in api.retweets? or api.get_status
origanl_user = 'Sukree'
G.add_node(origanl_user)
# G.add_node(all_users[0])
# G.add_edge(all_users[0],'Orignal')
# G.add_edge()

## check if A is following B
def isFollowing(userA, userB):
    followOrNot = api.show_friendship(source_screen_name = userA, target_screen_name = userB)
    return followOrNot[0].following


### revise this part, the user will retweet the first person instead of the last one
for i, user in enumerate(all_users):
    print i
    G.add_node(user)
    # # This is a reverse algorithm,
    # while i>=1:
    #     if isFollowing(user, all_users[i-1]):
    #         G.add_edge(user, all_users[i-1])
    #         break;
    #     else:
    #         i -=1
    # else:
    #     G.add_edge(user, origanl_user)
    # ###
    #### this is for a ordered search for friendship
    #set the flag to false
    # connected = False
    for compared_user in all_users[:i]:
        if isFollowing(user, compared_user):
            G.add_edge(user, compared_user)
            connected = True  # if found someone who the current user is following, then connect this node
            break;
    # if it is not connected:     # if the current user hasn't connected to any node, connect it to the orignal one
    else:
        G.add_edge(user, origanl_user)

# nx.draw(G,with_labels=True)
# plt.show()
# nx.layout
app = Viewer(G)
app.mainloop()