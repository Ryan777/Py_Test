#coding=utf-8#coding=utf-8
import tweepy
from local_config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

i = 0
# followers = api.followers_ids(id='alexandraizqRD')
ids =[]
for page in tweepy.Cursor(api.retweets, id='737827309466484738').pages():
    ids.extend(page)

print len(ids)
# print followers
#
# print len(followers)
