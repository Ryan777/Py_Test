import networkx as nx
import matplotlib.pyplot as plt
import mysql.connector

conn = mysql.connector.connect(user='root', password='777',
                              host='127.0.0.1',
                              database='Twitter',
                              charset = 'utf8mb4')

c = conn.cursor()

c.execute('Select User_name, Retweeted_user From Test')

data = c.fetchall()
G= nx.MultiDiGraph()

for row in data :
    G.add_node(row[0])
    if row[1] != "":
        G.add_node(row[1])
        G.add_edge(row[0],row[1])

# nx.draw(G,with_labels=True)
# plt.show()