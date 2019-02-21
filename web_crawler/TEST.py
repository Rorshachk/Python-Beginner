import urllib.request
import urllib.parse
import socket
import urllib
import urllib.error

from urllib import request, error
from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit


# Request
'''
response = urllib.request.urlopen("http://www.python.org")
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
'''

# Error
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
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
result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)
print(result.scheme, result[0])


result = urlparse('http://www.baidu.com', scheme='https')
print(result)

result = urlparse('https://www.baidu.com/index.html;user?id=5#comment',
                  allow_fragments=False)
print(result)

result = urlparse('https://www.baidu.com/index.html#comment',
                  allow_fragments=False)
print(result)


# unparse
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))

URL = urlunparse(data)

# split and unsplit
result = urlsplit(URL)
print(result)

data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))
