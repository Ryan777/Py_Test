'''
Created on Jan 10, 2559 BE

@author: Rampage
'''
import tweepy
from local_config import *
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

help(api)

####################
# #search for a user's status
# statuses = api.user_timeline(id = 55261782, count = 200)  # Ajarn Sukree... Empty parameter means myself
# for status in statuses:
#     print "***"
#     print "Tweet id: " + status.id_str
#     print status.text
#     print "Retweet count: " + str(status.retweet_count)
#     print "Favorite count: " + str(status.favorite_count)
#     print status.created_at
#     print "Status place: " + str(status.place)
#     print "Source: " + status.source
#     print "Coordinates: " + str(status.coordinates)
#      
#     time.sleep(1)
#########################
# #search for a certain place, 3376992a082d67c7 is Canada.
# #seems to have some problems here
# results = api.search(q = "place:3376992a082d67c7", count = 100)
# for result in results:
#         print result.coordinates['coordinates']