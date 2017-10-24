import requests
from bs4 import BeautifulSoup
import mysql.connector
import configparser

# 爬取 丑事百科 文章
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
    url = 'https://www.qiushibaike.com/text/page/' + str(x) + '/'
    res = requests.get(url, headers=headers).text
    soup = BeautifulSoup(res, 'html.parser', from_encoding='utf-8')
    tags = soup.find_all('div', class_="article")
    for tag in tags:
        tt = tag.find('a', class_='contentHerf')
        span = tt.div
        ct = span.find('span').get_text(strip=True)
        # p = tag.a.div.span.get_text()
        cursor.execute('insert into joke (content) values (%s)', [ct])
        # print(cursor.rowcount)
        # print(ct)
conn.commit()
cursor.close()
    # print(tags)