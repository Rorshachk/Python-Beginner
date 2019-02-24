import requests as rq

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
