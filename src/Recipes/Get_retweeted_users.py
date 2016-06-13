import tweepy
from local_config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

print (api.rate_limit_status())

tweetID = "724664541192306688"
status = api.get_status(tweetID)
# print "------Status---------"
# print status

### status.id = tweetID
retweets = api.retweets(status.id)
# print "---------Retweets---"
# print retweets
print "--------------"
print ("Tweet %s, originally posted by %s, was retweeted by..." % (status.id, status.user.screen_name))
for retweet in retweets:
    print (retweet.user.screen_name)
