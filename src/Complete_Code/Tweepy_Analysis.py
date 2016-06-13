'''
Created on Jan 11, 2559 BE

Search for a certain query and make a DataFrame , and print them
and select those timezone area are not null, plot them into a bar-graph
@author: Rampage
'''

import tweepy
import pandas as pd
import matplotlib.pyplot as plt
from local_config import *
import time


# Make the graphs prettier 
######this is a fucking bug!!!!
# pd.set_option('display.mpl_style', 'default')
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
 
# result = api.search(q="#Starwars")
# print len(result)
# tweet = result[0]
# print tweet
# for param in dir(tweet):
#     if not param.startswith('_'):
#         print "%s : %s\n" %(param, eval('tweet.'+param))
         
results = []
for tweet in tweepy.Cursor(api.search, q = "#Starwars").items(50):
    results.append(tweet)
#     time.sleep(1)
print(len(results))
 
def toDataFrame(tweets):
    DataSet = pd.DataFrame()
     
    DataSet['tweetID'] = [tweet.id for tweet in tweets]
    DataSet['tweetText'] = [tweet.text for tweet in tweets]
    DataSet['tweetRetweetCt'] = [tweet.retweet_count for tweet in tweets]
    DataSet['tweetFavoriteCt'] = [tweet.favorite_count for tweet in tweets]
    DataSet['tweetSource'] = [tweet.source for tweet in tweets]
    DataSet['tweetCreated'] = [tweet.created_at for tweet in tweets]
     
    DataSet['userID'] = [tweet.user.id for tweet in tweets]
    DataSet['userScreen'] = [tweet.user.screen_name for tweet in tweets]    
    DataSet['userName'] = [tweet.user.name for tweet in tweets]     
    DataSet['userCreateDt'] = [tweet.user.created_at for tweet in tweets]     
    DataSet['userDesc'] = [tweet.user.description for tweet in tweets]     
    DataSet['userFollowerCt'] = [tweet.user.followers_count for tweet in tweets]     
    DataSet['userFriendsCt'] = [tweet.user.friends_count for tweet in tweets]     
    DataSet['userLocation'] = [tweet.user.location for tweet in tweets]     
    DataSet['userTimezone'] = [tweet.user.time_zone for tweet in tweets]
     
    return DataSet
 
DataSet = toDataFrame(results)

# #print then to a csv file ( but there are some problems with it, displaying not good)
#  DataSet.to_csv('tweepy_analysis', sep='\t', encoding='utf-8')
# ## perfect idea to print pandas
#  with pd.option_context('display.max_rows', 999, 'display.max_columns', 20):
#      print DataSet
     
# 'None' is treated as null here, so I'll remove all the records having 'None' in their 'userTimezone' column 
DataSet = DataSet[DataSet.userTimezone.notnull()] 
# Let's also check how many records are we left with now
print  
print("There are "+str(len(DataSet))+" data left")
print 
 
# Count the number of tweets in each time zone and get the first 10 
tzs = DataSet['userTimezone'].value_counts()
print(tzs)
 
# Create a bar-graph figure of the specified size 
plt.rcParams['figure.figsize'] = (15, 5) 
# Plot the Time Zone data as a bar-graph 
tzs.plot(kind='bar') 
# Assign labels and title to the graph to make it more presentable 
plt.xlabel('Timezones') 
plt.ylabel('Tweet Count') 
plt.title('Top 10 Timezones tweeting about #Starwars')
 
plt.show()
 