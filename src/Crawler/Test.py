#coding=utf-8
import re
str = '下一个你需要输入的数字是57633. 老实告诉你吧, 这样的数字还有上百个'
print type(re.findall(r'\d+',str)[0])