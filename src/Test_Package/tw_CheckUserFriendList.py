'''
Created on Dec 21, 2558 BE

@author: Rampage
'''
import tweepy


auth = tweepy.OAuthHandler('7FWpTHkeQMaO1bnHQYnd62De8','albUzEWdlrpI9gP8uH7FcCHi1Cgo2QLeKSPLPqNVIAUMimM2Fa')
auth.set_access_token('2668995974-UKVj9CIcCF0zfIeCBRvIyOGqL1oPPi6OJ1fH1y6','g7TgKKOJ0Bj1ua7UvGnWT98ztvmzVXA72OIcd04OCifZU')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
user = api.get_user('Noey_Somrutai')
print user.screen_name
print 'You have '+ str(user.followers_count) +' followers, they are :'

for friend in user.followers():    
    # Process the friend here
    print friend.screen_name
