import mysql.connector
import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
# py.sign_in('username','api_key')


conn = mysql.connector.connect(user='root', password='777',
                              host='127.0.0.1',
                              database='Twitter',
                              charset = 'utf8mb4')
cursor = conn.cursor()

cursor.execute("Select User_name, Retweeted_user, time from เที่ยงรายวัน")
rows = cursor.fetchall()
print(rows)


df = pd.DataFrame([[ij for ij in i] for i in rows])
df.rename(columns={0 : "User_name", 1 : "Retweeted_user", 2: "time"}, inplace=True)


trace1 = go.Scatter(
    x = df['time'],
    y = df['Retweeted_user'],
    text = "User_nameR",
)
layout = go.Layout(
    xaxis = go.XAxis(title ='time'),
    yaxis = go.YAxis(title = 'Retweeted_user')
)

data = go.Data([trace1])
fig = go.Figure(data= data, layout=layout)
plotly.offline.plot(fig,filename = "hello world")