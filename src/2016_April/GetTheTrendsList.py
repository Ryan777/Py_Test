'''
Created on Jan 3, 2559 BE

@author: Rampage
'''

## trends --- list with only one element
## trends[0] --- dict , there is a 'trends' element in it
## trends[0]['trend'] ---list, with all the trends details, trends[0]['trend'][1] / [50] etc,

# #####    for trend in trends[0]["trends"]:
# #####        print(trend['name'])

# autopep8 tweepy2016.py -i -a



import tweepy
from local_config import *
import json

# if __name__ == "__main__":      ####what is this for?

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
twitter_api = tweepy.API(auth)

    # Search stuff
#     search_results = tweepy.Cursor(twitter_api.search, q = "Python").items(5)
#     for result in search_results:
#         print(result.text)

# trends = twitter_api.trends_place(23424960)

# for trend in trends[0]["trends"]:
#     print(trend['name'])
# #     print(type(trends))
# #     print(type(trends[0]))
# #     print(type(trends[0]['trends']))
# #     print(type(trends[0]['trends'][0]))
# #     print(type(trends[0]['trends'][0]['name']))
# #     print(trends[0])

##useful!!!!!!!!!!
print(json.dumps(twitter_api.trends_place(23424960), indent=1))

### has some problems here, but it is a good idea
# myTrends = [
#     trend['name']
#         for trend in twitter_api.trends_place(23424960)['trends']
# ]
####



# print(trends)