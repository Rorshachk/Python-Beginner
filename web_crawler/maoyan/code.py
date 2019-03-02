import requests as rq
import re
import time
from requests.exceptions import RequestException
import json


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
    items = re.findall('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star">\n(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', html, re.S)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3],
            'time': item[4],
            'score': item[5] + item[6]
        }


def write_to_file(item):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')


def main():
    base_url = 'https://maoyan.com/board/4/?offset='
    for i in range(10):
        html = get_one_page(base_url + str(i * 10))
        for item in parse_one_page(html):
            print(item)
            write_to_file(item)
        time.sleep(1)


main()
