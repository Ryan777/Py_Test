#encoding=utf8
import mysql.connector
conn = mysql.connector.connect(user='root', password='777',
                              host='127.0.0.1',
                              database='Proposal',
                              charset = 'utf8mb4')
# change charset to utf8mb4
c = conn.cursor()


# c.execute("SELECT User_id FROM `Marilyn Monroe` where Original_id = '738025281764659200';")
# retweeter_ids_temp = c.fetchall()
# all_retweeters = []
# for user in retweeter_ids_temp:
#     all_retweeters.append(user[0])
#
# print type(all_retweeters)
# print all_retweeters
#
# # if '97436705' in all_retweeters:
# #     print "yes"
# print type(all_retweeters[0])

### check if a user is already in the database

# def Check_in_DB(user_id):
#     # uid = user_id
#     c.execute("select 1 from `Fellowship` where User_ID = "+user_id+" limit 1;")
#     result = c.fetchone()
#     print result
#     if result == (1,):
#         return True
#     else:
#         return False
#
# print Check_in_DB('97319110')
#
# c.execute("SELECT User_id FROM `Paul Ryan` where Original_id = '738567224600858625' ORDER BY Local_Time;")
# retweeter_ids_temp = c.fetchall()
# all_retweeters = []
# for user in retweeter_ids_temp:
#     all_retweeters.append(int(user[0]))
# print all_retweeters[35],all_retweeters[36],all_retweeters[37],all_retweeters[38]
# print "There are "+ str(len(all_retweeters))+" retweeters in total!"



## get user's followers
userID = '97319119'
c.execute("SELECT Follower_ID FROM `Fellowship` where User_ID = "+ userID)
followers_id_tmp = c.fetchall()
followers = []
for user in followers_id_tmp:
    followers.append(int(user[0]))
print "There are "+ str(len(followers))+" retweeters in total!"
followers = set(followers)
print len(followers)