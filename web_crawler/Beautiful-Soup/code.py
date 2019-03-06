import requests as rq
import re
import time
from requests.exceptions import RequestException
import json
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
            'index': movie.select('.board-index')[0].get_text(),
            'image': movie.select('.board-img')[0]['data-src'],
            'title': movie.select('.name')[0].select('a')[0].get_text(),
            'actor': movie.select('.star')[0].get_text(),
            'time': movie.select('.releasetime')[0].get_text(),
            'score': movie.select('.score')[0].select('i')[0].get_text() + movie.select('.score')[0].select('i')[1].get_text()
        }


def write_to_file(item):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')


def main():
    base_url = 'https://maoyan.com/board/4/?offset='
    for i in range(10):
        html = get_one_page(base_url + str(i * 10))
        parse_one_page(html)

        for item in parse_one_page(html):
            print(item)
            write_to_file(item)

        time.sleep(1)


main()
