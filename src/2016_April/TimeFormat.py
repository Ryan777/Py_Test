# import datetime
import time

dict= {"timestamp_ms": "1403907978000"}
# print(datetime.datetime.fromtimestamp(int("1403907978000")/1000).strftime('%Y-%m-%d %H:%M:%S'))
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(int(time.time()) / 1000.0)))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))))
# print(time.localtime(time.time()))
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(1460976771676/1000.0)))