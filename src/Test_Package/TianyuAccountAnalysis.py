'''
Created on Dec 23, 
#testtttttt222222222
@author: Rampage
'''
# handle = open('test.txt','r')
# # content = handle.readline()
# print content
# #get a list of [number,date]
# contentList = [content.split()[2()[5].split('-')[1]]

# # print contentList
# data = dict()
# data[contentList[1]]=contentList[0]
# print data        
import calendar
# str = '03'
# month = calendar.month_name[int(str)]
# print month

data = dict()

with open('tianyuaccounts1.txt','r') as f:
    for line in f:
        content = line.rstrip()
        # print content
        #get a list of [account number, digtal month], such as ['999999999999','03']
        contentList = [content.split()[2],content.split()[5].split('-')[1]]
        #change the number of month to the name of month
        date = calendar.month_name[int(contentList[1])]

        if date not in data:
            data[date] = [contentList[0]]
        else:
            data[date].append(contentList[0])
# print data
print 'Data analysis for Tian yu accounts (basic accounts)\n' 
for key,value in data.items():
    print key
    print value
    print 'The amount of accounts is : ',len(value)
    print 