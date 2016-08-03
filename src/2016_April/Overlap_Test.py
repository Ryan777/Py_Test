#coding=utf-8
from local_config import *
import networkx as nx
import mysql.connector

conn = mysql.connector.connect(user='root', password='777',
                              host='127.0.0.1',
                              database='Proposal',
                              charset = 'utf8mb4')
c = conn.cursor()


c.execute("SELECT User_id FROM `Phones` where Original_id = '745357701891371008' ORDER BY Local_Time;")

retweeter_ids_temp = c.fetchall()
retweeters_1 = []
for user in retweeter_ids_temp:
    retweeters_1.append(int(user[0]))

# print type(retweeters_1)
# print retweeters_1
print len(retweeters_1)


G = nx.DiGraph()
G.add_node('original_1', color = 'black')
for retweeter in retweeters_1:
    G.add_node(retweeter,color="green")
    G.add_edge(retweeter,'original_1')



c.execute("SELECT User_id FROM `Phones` where Original_id = '745312202312261632' ORDER BY Local_Time;")

retweeter_ids_temp = c.fetchall()
retweeters_2 = []
for user in retweeter_ids_temp:
    retweeters_2.append(int(user[0]))

print len(retweeters_2)
# print type(retweeters_2)
# print retweeters_2

G.add_node('original_2', color = 'black')
red_count = 0
for retweeter_2 in retweeters_2:
    if retweeter_2 in retweeters_1:
        G.add_node(retweeter_2,color = 'red')
        G.add_edge(retweeter_2,'original_2')
        red_count+=1
    else:
        G.add_node(retweeter_2,color = 'blue')
        G.add_edge(retweeter_2,'original_2')


print nx.get_node_attributes(G,'color')
print red_count
nx.write_graphml(G,path = '/Users/Rampage/movies/Overlap1.graphml')