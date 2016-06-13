'''
Created on Jan 3, 2559 BE

@author: Rampage
'''

## trends --- list with only one element
## trends[0] --- dict , there is a 'trends' element in it 
## trends[0]['trend'] ---list, with all the trends details, trends[0]['trend'][1] / [50] etc,

# autopep8 tweepy2016.py -i -a
import tweepy
from local_config import *

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    twitter_api = tweepy.API(auth)
 
    # Search stuff
#     search_results = tweepy.Cursor(twitter_api.search, q = "Python").items(5)
#     for result in search_results:
#         print(result.text)
 
    trends = twitter_api.trends_place(1)
 
#     for trend in trends[0]["trends"]:
#         print(trend)
    print(type(trends))
    print(type(trends[0]))
    print(len(trends[0]['trends']))
    print(type(trends[0]['trends'][0]))
    print(type(trends[0]['trends'][0]['name']))
    print(trends[0])
