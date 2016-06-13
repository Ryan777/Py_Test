#coding=utf-8
import tweepy
from local_config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


## Check if userA follows userB, for screen_name, it is not case- sensitive
def isFollowing(userA, userB):
    followOrNot = api.show_friendship(source_screen_name = userA, target_screen_name = userB)
    print followOrNot
    return followOrNot[0].following



print isFollowing('maerdcha','Sukree')