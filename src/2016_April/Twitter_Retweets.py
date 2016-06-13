### Get the retweeter names from a specific tweet, but it seems not complete,
# like it is said 66 retweet times, but I got only 58 names

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
import time
import json
from local_config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# "count" is the number of the retweets, up to 100
retweets = api.retweets(id = 730695291641466880, count =100)
i = 0
for retweet in retweets:
    # user_mention = ""
    # print retweet.created_at + " From "+ retweet.user.screen_name +" to " + retweet.user_mentions.screen_name
    print retweet.created_at
    if user_mentions.screen_name in retweet:
        print retweet.user_mentions.screen_name
    print retweet.user.screen_name

    i= i+1

print i