#coding=utf-8
import tweepy

import mysql.connector
conn = mysql.connector.connect(user='root', password='777',
                              host='127.0.0.1',
                              database='Proposal',
                              charset = 'utf8mb4')
# change charset to utf8mb4
c = conn.cursor()

auth = tweepy.AppAuthHandler('7FWpTHkeQMaO1bnHQYnd62De8', 'albUzEWdlrpI9gP8uH7FcCHi1Cgo2QLeKSPLPqNVIAUMimM2Fa')
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)



def Check_in_DB(user_id):
    # uid = user_id
    c.execute("select 1 from `Fellowship_Jun` where User_ID = "+str(user_id)+" limit 1;")
    result = c.fetchone()
    # print result
    if result == (1,):
        return True
    else:
        return False




# uname = ""
# user_id = "249346453"
#
# followers =[]
# for page in tweepy.Cursor(api.followers_ids, id= user_id, count = 5000).pages():
#     followers.extend(page)
# print len(followers)
# # print followers
# print "--------------------"
# store the followers into database


### !!!! maybe the problem is there have to check every record in database
# for follower in followers:
#     # c.execute("INSERT INTO Fellowship (User_ID, Follower_ID) VALUES (%s,%s)",(original_user_id, follower))
#     c.execute("INSERT INTO Fellowship (User_ID, Follower_ID) SELECT %s, %s FROM DUAL WHERE NOT EXISTS(SELECT User_ID,Follower_ID FROM Fellowship WHERE User_ID = %s &&Follower_ID = %s);",(user_id,follower,user_id,follower))
# conn.commit()


c.execute("SELECT User_id FROM `To_be_analyzed` where Original_id = '745180604459671552' ORDER BY Local_Time;")
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
        followers =[]
        for page in tweepy.Cursor(api.followers_ids, id= retweeter, count = 5000).pages():
            followers.extend(page)
        # print len(followers)
        print "User "+str(retweeter)+" has "+str(len(followers))+ " followers"
        i = 0
        for follower in followers:
            c.execute("INSERT INTO Fellowship_Jun (User_ID, Follower_ID) VALUES (%s,%s)",(retweeter, follower))
            i+=1
        conn.commit()
        print "Inserted the followers of "+str(retweeter)+" into database"
        recorded_user+=1
        print "Imported "+str(recorded_user)+ " users by now"

