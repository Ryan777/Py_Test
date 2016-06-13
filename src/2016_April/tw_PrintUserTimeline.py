'''
Created on Dec 21, 2558 BE

@author: Rampage
'''

import tweepy


auth = tweepy.OAuthHandler('7FWpTHkeQMaO1bnHQYnd62De8','albUzEWdlrpI9gP8uH7FcCHi1Cgo2QLeKSPLPqNVIAUMimM2Fa')
auth.set_access_token('2668995974-UKVj9CIcCF0zfIeCBRvIyOGqL1oPPi6OJ1fH1y6','g7TgKKOJ0Bj1ua7UvGnWT98ztvmzVXA72OIcd04OCifZU')

api = tweepy.API(auth)
# api.friends()
# public_tweets = api.home_timeline()
user = api.get_user('Noey_Somrutai')
print(user.id)


# Iterate through all of the authenticated user's friends
# for tweet in tweepy.Cursor(api.user_timeline, id='Noey_Somrutai').items():
for tweet in api.user_timeline('Noey_Somrutai'):
#in sublime, I need to encode, but not in Eclipse, why?
#encoding to display Thai language
    print(tweet.text.encode('utf-8'))