import requests as rq
from urllib.parse import urlencode
import os
from hashlib import md5
from bs4 import BeautifulSoup
import re
import json
from pymongo import MongoClient
from multiprocessing import Pool

client = MongoClient()
db = client['toutiao']
collection = db['toutiao']


def get_page(offset):
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': '1553345465205',
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    print(url)
    try:
        response = rq.get(url)
        if response.status_code == 200:
            return response.json()
    except rq.ConnectionError:
        return None


def parse_page(json):
    data = json.get('data')
    if data == None:
        return None
    for item in data:
        if item.get('article_url') != None:
            yield item.get('article_url')


def get_page_detail(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    try:
        response = rq.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except rq.ConnectionError:
        return None


def parse_page_detail(html, url):
    if html == None:
        return None
    else:
        soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
#    print(title)
    image_patterns = re.compile('gallery:\sJSON.parse\("(.*?)"\)', re.S)
    result = re.search(image_patterns, html)
    if result:
        data = result.group(1).replace('\\', '')
        data = json.loads(data)
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images:
                download_image(image)
            return {
                'title': title,
                'url': url,
                'images': images
            }


def save_to_Mongo(result):
    if db['toutiao'].insert(result):
        print('Mongo Successful')
        return True
    else:
        print('False')
        return False


def download_image(url):
    print("downloading pic:", url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    try:
        response = rq.get(url, headers=headers)
        if response.status_code == 200:
            save_image(response.content)
    except rq.ConnectionError:
        return None


def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd(),
                                     md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()


def main(offset):
    json = get_page(offset)
    print(offset)
    for url in parse_page(json):
        html = get_page_detail(url)
        result = parse_page_detail(html, url)
        if result:
            save_to_Mongo(result)


if __name__ == '__main__':
    groups = [x * 20 for x in range(0, 10)]
    pool = Pool()
    pool.map(main, groups)
