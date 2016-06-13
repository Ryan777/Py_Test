import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import mysql.connector
import networkx as nx
import matplotlib.pyplot as plt

conn = mysql.connector.connect(user='root', password='777',
                              host='127.0.0.1',
                              database='Twitter',
                              charset = 'utf8mb4')
# change charset to utf8mb4
c = conn.cursor()


ckey='7FWpTHkeQMaO1bnHQYnd62De8'
csecret='albUzEWdlrpI9gP8uH7FcCHi1Cgo2QLeKSPLPqNVIAUMimM2Fa'
atoken='2668995974-UKVj9CIcCF0zfIeCBRvIyOGqL1oPPi6OJ1fH1y6'
asecret='g7TgKKOJ0Bj1ua7UvGnWT98ztvmzVXA72OIcd04OCifZU'

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)




all_users = [u'sagez9master', u'PanJ', u'f_takco', u'pawin35', u'AmiHirari', u'LINTANIA', u'maerdcha', u'ShitNigSays', u'mookcifer']
print all_users


G= nx.MultiDiGraph()
### I should add some code to identify the orignal user's name instead of calling him 'Orignal', can I do it in api.retweets? or api.get_status
origanl_user = 'Sukree'
G.add_node(origanl_user)
# G.add_node(all_users[0])
# G.add_edge(all_users[0],'Orignal')
# G.add_edge()
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
    # if not connected:     # if the current user hasn't connected to any node, connect it to the orignal one
    else:
        G.add_edge(user, origanl_user)

nx.draw(G,with_labels=True)
plt.show()
nx.layout