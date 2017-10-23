import requests
from bs4 import BeautifulSoup
import mysql.connector


# 连接数据库
conn = mysql.connector.connect(user='root', password='xy521521', database='xy')
cursor = conn.cursor()
# 爬取 内涵段子
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
url = 'http://neihanshequ.com'
res = requests.get(url, headers=headers).text
soup = BeautifulSoup(res, 'html.parser', from_encoding='utf-8')
tags = soup.find_all('div', class_="upload-txt no-mb")
for tag in tags:
    p = tag.h1.p.get_text()
    cursor.execute('insert into joke (content) values (%s)', [p])
    # print(cursor.rowcount)
    # print(p)
conn.commit()
cursor.close()
# print(tags)