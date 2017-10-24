import requests
import mysql.connector
import configparser

cf = configparser.ConfigParser()
cf.read("../db.conf")
db_user = cf.get("db", "db_user")
db_pwd = cf.get("db", "db_pwd")
# 连接数据库
conn = mysql.connector.connect(user=db_user, password=db_pwd, database='xy')
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