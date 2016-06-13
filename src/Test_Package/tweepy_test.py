
# #1. Initialize your private stuff 
# consumer_key = '7FWpTHkeQMaO1bnHQYnd62De8'
# consumer_secret = 'albUzEWdlrpI9gP8uH7FcCHi1Cgo2QLeKSPLPqNVIAUMimM2Fa'
# access_token = '2668995974-UKVj9CIcCF0zfIeCBRvIyOGqL1oPPi6OJ1fH1y6'
# access_token_secret = 'g7TgKKOJ0Bj1ua7UvGnWT98ztvmzVXA72OIcd04OCifZU'


import tweepy


auth = tweepy.OAuthHandler('7FWpTHkeQMaO1bnHQYnd62De8','albUzEWdlrpI9gP8uH7FcCHi1Cgo2QLeKSPLPqNVIAUMimM2Fa')
auth.set_access_token('2668995974-UKVj9CIcCF0zfIeCBRvIyOGqL1oPPi6OJ1fH1y6','g7TgKKOJ0Bj1ua7UvGnWT98ztvmzVXA72OIcd04OCifZU')

api = tweepy.API(auth)
# api.friends()
# public_tweets = api.home_timeline()
user = api.get_user('Noey_Somrutai')
print(user.screen_name)
print('You have')
print(user.followers_count),
print ('friends')
# Iterate through all of the authenticated user's friends
for tweet in tweepy.Cursor(api.user_timeline,id='Noey_Somrutai').items():
    print(tweet)
    print("--------------------")
# help(user)
# for friend in user.friends():
#     # Process the friend here
#     print friend.screen_name
# for status in tweepy.Cursor(api.friends_timeline).items(7):
#     print (tweet.text)

# for friend in user.friends():
#     print friend.screen_name
# for tweet in public_tweets:
#     print (tweet.text)

