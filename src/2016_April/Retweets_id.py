import tweepy
from local_config import *
import mysql.connector
conn = mysql.connector.connect(user='root', password='777',
                              host='127.0.0.1',
                              database='Proposal',
                              charset = 'utf8mb4')
# change charset to utf8mb4
c = conn.cursor()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


retweets = api.retweets(id = 363644399416119296, count =100)
i = 0
# print type(retweets)
# all_users = {}
all_retweeters = []
for retweet in retweets:
    # user_mention = ""
    # print retweet.created_at + " From "+ retweet.user.screen_name +" to " + retweet.user_mentions.screen_name
    print retweet.created_at
    print retweet.user.id ### latest comes first. 2015, 2014, 2013  ## id or screen_name
    # all_users[retweet.user.screen_name]= retweet.created_at
    all_retweeters.append(retweet.user.id)
    i= i+1

all_retweeters.reverse()


def Check_in_DB(user_id):
    # uid = user_id
    c.execute("select 1 from `Fellowship` where User_ID = "+str(user_id)+" limit 1;")
    result = c.fetchone()
    # print result
    if result == (1,):
        return True
    else:
        return False
recorded_user = 0

for retweeter in all_retweeters:
    if Check_in_DB(retweeter):
        print "This user "+ str(retweeter)+ " is already in the database"
        continue
    else:
        followers =[]
        for page in tweepy.Cursor(api.followers_ids, id= retweeter, count = 5000).pages():
            followers.extend(page)
        print len(followers)
        i = 0
        for follower in followers:
            c.execute("INSERT INTO Fellowship (User_ID, Follower_ID) VALUES (%s,%s)",(retweeter, follower))
            i+=1
        conn.commit()
        print "Insert "+str(i)+" data"
        recorded_user+=1
        print "Imported "+str(recorded_user)+ " users by now"

