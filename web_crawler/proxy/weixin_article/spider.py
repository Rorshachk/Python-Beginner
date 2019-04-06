import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq
from pymongo import MongoClient

base_url = 'http://weixin.sogou.com/weixin?'

headers = {
    'Cookie': 'SUV=00432718080C11EE5B255EA7ACCA7586; CXID=8B95202FDAECCABC73CDCD5AA761D512; SUID=66B7D8735E68860A5A99567100042826; usid=hP9LUnMneJVRfnuT; ssuid=1216583034; wuid=AAFLpiSNIQAAAAqLFD3bWQEAGwY=; GOTO=Af41001; UM_distinctid=16803251f4818d-0beb6cb9319f9d-b781636-1fa400-16803251f49b69; SMYUV=1546240991157276; sw_uuid=5469976730; start_time=1547560685826; pgv_pvi=9260803072; sg_uuid=3094649002; ld=bkllllllll2ttv5hlllllVhk577lllllKgcbNlllll9lllll4Zlll5@@@@@@@@@@; ABTEST=8|1554474269|v1; weixinIndexVisited=1; sct=2; JSESSIONID=aaag_j0YwtF4-7GHUvDNw; PHPSESSID=9dlp5vsvlrptb804s0q7j61s22; SUIR=B75249D8ABAF2F63950A5E06ABEA58E5; SNUID=A94D56C6B5B0307CDC71A8BDB5003F69; IPLOC=CN3310; ppinf=5|1554475526|1555685126|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo1OmN6aG5ifGNydDoxMDoxNTU0NDc1NTI2fHJlZm5pY2s6NTpjemhuYnx1c2VyaWQ6NDQ6bzl0Mmx1TWpDQnAzYkNJOW13My1yU3FHLUVSa0B3ZWl4aW4uc29odS5jb218; pprdig=My0WgbLQsJZrbtJ6DIzdWajyFh32k2UO12SJtVFW8oT3adCRq5hi_N_00-OZC3IjSR7-zac0ZxrBppqPYnSPwcQlHbeJePqWEJMj1w7fVheBIeh8BBubfQY5spvXL2fhAVT8rg6iB8RzAyDkMB02OVk8tYgj8dEztSm_XG7Pv_E; sgid=30-39971531-AVynagb6JbowKTSQaFSWic0c; ppmdig=1554475527000000b9992100eb5b9c6f1f02b1b67d49111b',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
}


proxy = None
max_count = 5


def get_proxy():

    proxy_host = 'http-dyn.abuyun.com'
    proxy_port = '9020'

    proxy_user = 'HQ9E9U80AEBW20KD'
    proxy_pass = 'F99D07889C887510'

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxy_host,
        "port": proxy_port,
        "user": proxy_user,
        "pass": proxy_pass,
    }
    return proxyMeta


def parse_idex(html):
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('data-share')


def parse_passage(html):
    doc = pq(html)
    title = doc('.rich_media_title').text()
    content = doc('.rich_media_content').text()
    author_name = doc('.profile_nickname').text()
    wechat_id = doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
    return {
        'title': title,
        'content': content,
        'author_name': author_name,
        'wechat_id': wechat_id
    }


def get_html(url, count=1):
    print('Crawling', url)
    print('Trying Count', count)
    global proxy

    if count >= max_count:
        print('Tried too many counts')
        return None

    try:
        if proxy:
            proxies = {
                'http': proxy
            }
            response = requests.get(
                url, allow_redirects=False, headers=headers, proxies=proxies)
        else:
            response = requests.get(
                url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            print(response.status_code)
#           print(response.text)
            proxy = get_proxy()
            if proxy:
                print('Using proxy', proxy)
                return get_html(url, count)
            else:
                print('get proxy failed')
                return None

    except ConnectionError as e:
        print('Error', e.args)
        proxy = get_proxy()
        count += 1
        return get_html(url, count)


def get_idex(keyword, page_number):
    params = {
        'query': keyword,
        'type': 2,
        'page': page_number
    }
    url = base_url + urlencode(params)
    html = get_html(url)
    return html


client = MongoClient()
db = client['wechat']
db.drop_collection('wechat')
collection = db['wechat']


def save_to_Mongo(result):
    if collection.insert(result):
        print('save to Mongo')


def main():
    for page in range(1, 101):
        html = get_idex('NBA', page)
#        print(html)
        if html:
            article_urls = parse_idex(html)
            for article_url in article_urls:
                response = requests.get(article_url)
                print(article_url)
                result = parse_passage(response.text)
                save_to_Mongo(result)


if __name__ == '__main__':
    main()
