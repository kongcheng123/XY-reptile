import requests
from bs4 import BeautifulSoup
import mysql.connector
import configparser

# 爬取 丑事百科 图片
cf = configparser.ConfigParser()
cf.read("../db.conf")
db_user = cf.get("db", "db_user")
db_pwd = cf.get("db", "db_pwd")
# 连接数据库
conn = mysql.connector.connect(user=db_user, password=db_pwd, database='xy')
cursor = conn.cursor()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
for x in range(14):
    url = 'https://www.qiushibaike.com/imgrank/page/' + str(x) + '/'
    res = requests.get(url, headers=headers).text
    soup = BeautifulSoup(res, 'html.parser', from_encoding='utf-8')
    tags = soup.find_all('div', class_="article")
    for tag in tags:
        tt = tag.find('div', class_='thumb')
        span = tt.a
        ct = span.img.attrs['src']
        result = 'https:'+ct
        # p = tag.a.div.span.get_text()
        cursor.execute('insert into picture (util) values (%s)', [result])
        # print(cursor.rowcount)
        print(result)
conn.commit()
cursor.close()
    # print(tags)