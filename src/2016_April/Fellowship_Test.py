#coding=utf-8
import tweepy
from local_config import *
import mysql.connector
import time
conn = mysql.connector.connect(user='root', password='777',
                              host='127.0.0.1',
                              database='Proposal',
                              charset = 'utf8mb4')
# change charset to utf8mb4
c = conn.cursor()

auth = tweepy.OAuthHandler(consumer_key7, consumer_secret7)
auth.set_access_token(access_token7, access_secret7)

api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

def Check_in_DB(user_id):
    # uid = user_id
    print "before check"
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    c.execute("select 1 from `Fellowship_Test` where User_ID = "+str(user_id)+" limit 1;")
    print "middle check"
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    result = c.fetchone()
    # print result
    print "after check"
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print
    if result == (1,):
        return True
    else:
        return False


c.execute("SELECT User_id FROM `To_be_analyzed` where Followers_count < 4000 ORDER BY Local_Time;")
retweeter_ids_temp = c.fetchall()
all_retweeters = []
for user in retweeter_ids_temp:
    all_retweeters.append(int(user[0]))
print "There are "+ str(len(all_retweeters))+" retweeters in total!"

recorded_user = 0

for retweeter in all_retweeters:
    if Check_in_DB(retweeter):
        print "This user "+ str(retweeter)+ " is already in the database"
        continue
    else:
        try:
            followers =[]
            for page in tweepy.Cursor(api.followers_ids, id= retweeter, count = 5000).pages():
                followers.extend(page)
            # print len(followers)
            print "User "+str(retweeter)+" has "+str(len(followers))+ " followers"
            i = 0
            if len(followers)==0:   ### this user doesn't have any followers.
                c.execute("INSERT INTO Fellowship_Test (User_ID, Follower_ID) VALUES (%s,%s)",(retweeter, '0'))
            else:
                for follower in followers:
                    c.execute("INSERT INTO Fellowship_Test (User_ID, Follower_ID) VALUES (%s,%s)",(retweeter, follower))
                    i+=1
            conn.commit()
            # print "Insert "+str(i)+" data"
            print "Inserted the followers of "+str(retweeter)+" into database"
            recorded_user+=1
            print "Imported "+str(recorded_user)+ " users by now"
            print
        except tweepy.TweepError:  ## This user is a protected account.
            print "The user "+ str(retweeter)+" is a protected account!"
            c.execute("INSERT INTO Fellowship_Jun (User_ID, Follower_ID) VALUES (%s,%s)",(retweeter, '0'))
            conn.commit()
