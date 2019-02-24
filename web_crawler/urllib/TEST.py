import urllib.request
import urllib.parse
import socket
import urllib
import urllib.error

from urllib import request, error
import urllib.parse as up
import http.cookiejar
from urllib.robotparser import RobotFileParser

# urlopen
'''
response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))
print(type(response))
'''

'''
response = urllib.request.urlopen("http://www.python.org")
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
'''


data = bytes(up.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen(
    'https://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(up.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')

response = request.urlopen(req)
print(response.read().decode('utf-8'))


# Error
data = bytes(up.urlencode({'word': 'hello'}), encoding='utf8')
try:
    response = urllib.request.urlopen(
        'https://httpbin.org/post', data=data, timeout=0.01)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')


try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')


try:
    response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')


# parse
result = up.urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)
print(result.scheme, result[0])


result = up.urlparse('http://www.baidu.com', scheme='https')
print(result)

result = up.urlparse('https://www.baidu.com/index.html;user?id=5#comment',
                     allow_fragments=False)
print(result)

result = up.urlparse('https://www.baidu.com/index.html#comment',
                     allow_fragments=False)
print(result)


# unparse
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(up.urlunparse(data))

URL = up.urlunparse(data)

# split and unsplit
result = up.urlsplit(URL)
print(result)

data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(up.urlunsplit(data))

# url join
# urljoin(base_url, new_url)
# Only scheme,netloc,path works
print(up.urljoin('http://www.baidu.com', 'FAQ.html'))
print(up.urljoin('http://www.baidu.com', 'http://cuiqingcai.com/FAQ.html'))
print(up.urljoin('http://www.baidu.com/about.html',
                 'http://cuiqingcai.com/FAQ.html'))
print(up.urljoin('http://www.baidu.com?wd=abc',
                 'http://cuiqingcai.com/index.php'))
print(up.urljoin('www.baidu.com', '?category=2#comment'))
print(up.urljoin('www.baidu.com#comment', '?category=2'))


# urlencode
# build GET
params = {
    'name': 'germey',
    'age': 22
}
base_url = 'http://www.baidu.copm?'
url = base_url + up.urlencode(params)
print(url)

# parse_qs and pars_qsl
query = ('name=germey&age=22')
print(up.parse_qs(query))
print(up.parse_qsl(query))


# quote and unquote
keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + up.quote(keyword)
print(url)
print(up.unquote(url))


# Cookies
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + '=' + item.value)

file_name = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(file_name)
cookie = http.cookiejar.LWPCookieJar(file_name)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

cookie = http.cookiejar.LWPCookieJar(file_name)

cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')


# print(response.read().decode('utf-8'))
with open('source.html', 'w', encoding='utf-8') as file_object:
    file_object.write(response.read().decode('utf-8'))

# Robot
rp = RobotFileParser(url='http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch
      ('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))
