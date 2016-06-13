#coding=utf-8

all = [1,2,3,4]
unfound = set(all)

followers = set(['4','5'])

a = all[0]

# # 集合无序 不重复 . 交集 差集
result = unfound & followers
print result