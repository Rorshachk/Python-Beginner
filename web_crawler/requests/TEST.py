import requests as rq
import re

r = rq.get('http://www.baidu.com')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

r = rq.get('http://httpbin.org/get')
print(r.text)

data = {
    'name': 'germey',
    'age': 22
}
r = rq.get('http://httpbin.org/get', params=data)
print(r.text)

r = rq.get('http://httpbin.org/get')
print(type(r.text))
print(r.json())
print(type(r.json()))

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = rq.get("https://www.zhihu.com/explore", headers=headers)
print(r.text)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)

r = rq.get('https://github.com/favicon.ico')
with open('favicon.ico', 'wb') as f_obj:
    f_obj.write(r.content)
