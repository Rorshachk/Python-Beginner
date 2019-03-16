import pymysql
import requests as rq
import time
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    try:
        response = rq.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    soup = BeautifulSoup(html, 'lxml')

    for movie in soup.find_all(name='dd'):
        yield {
            'id': movie.select('.board-index')[0].get_text(),
            'image': movie.select('.board-img')[0]['data-src'],
            'title': movie.select('.name')[0].select('a')[0].get_text(),
            'actor': movie.select('.star')[0].get_text(),
            'time': movie.select('.releasetime')[0].get_text(),
            'score': movie.select('.score')[0].select('i')[0].get_text() + movie.select('.score')[0].select('i')[1].get_text()
        }


def write_to_file(item):
    db = pymysql.connect(host='localhost', user='root',
                         password='hsm20011210', port=3306, db='spiders')
    cursor = db.cursor()
    table = 'movies'
    keys = ', '.join(item.keys())
    values = ', '.join(['%s'] * len(item))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(
        table=table, keys=keys, values=values)
    print(sql)
    print(item.values())

    try:
        #    sql = 'INSERT INTO movies(idex, image, title, actor, time, score) values(%s, %s, %s, %s, %s, %s)'
        if cursor.execute(sql, tuple(item.values())):
            print('successful')
            db.commit()

    except:
        print('failed')
        db.rollback()
    db.close()


def main():
    base_url = 'https://maoyan.com/board/4/?offset='
    for i in range(10):
        html = get_one_page(base_url + str(i * 10))

        for item in parse_one_page(html):
            #         print(item)
            write_to_file(item)

        time.sleep(1)

'''
db = pymysql.connect(host='localhost', user='root',
                     password='hsm20011210', port=3306, db='spiders')
cursor = db.cursor()
cursor.execute('drop tables movies')
# mysql里 index是保留字
sql = 'CREATE TABLE IF NOT EXISTS movies (id INT NOT NULL, image VARCHAR(255), title VARCHAR(255), actor VARCHAR(255), time VARCHAR(255), score FLOAT, PRIMARY KEY (id))'
cursor.execute(sql)
db.close()
'''


'''
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print(data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8mb4")
db.close()
'''

# main()

db = pymysql.connect(host='localhost', user='root',
                     password='hsm20011210', port=3306, db='spiders')
cursor = db.cursor()
table = 'movies'
condition = 'score > 9.0'
sql = 'SELECT * FROM movies WHERE score >= 9.5'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')
