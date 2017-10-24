import requests
import mysql.connector

# 连接数据库
conn = mysql.connector.connect(user='root', password='xy521521', database='xy')
cursor = conn.cursor()
for x in range(325):
    cursor.execute('select * from picture where id = %s', (x+1,))
    values = cursor.fetchall()
    # print(values)
    print(values[0][1])
    url = values[0][1]
    r = requests.get(url)
    with open('../pc/' + str(x) + '.jpg', 'wb') as outfile:
      outfile.write(r.content)