'''
Created on Jan 14, 2559 BE

@author: Rampage
'''

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(('www.pythonlearn.com',80))

mySocket.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mySocket.recv(512)
    if (len(data) < 1) : 
        break
    print data
    
mySocket.close()