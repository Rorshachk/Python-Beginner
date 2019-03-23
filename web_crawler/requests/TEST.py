import requests as rq
import re
from requests import Request, Session

r = rq.get('https://www.toutiao.com/a6671142904460739075/')
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

r = rq.post('http://httpbin.org/post', data=data)
print(r.text)

r = rq.get('http://jianshu.com', headers=headers)
print(r.status_code, type(r.status_code))
print(r.headers, type(r.headers))
print(r.cookies, type(r.cookies))
print(r.url, type(r.url))
print(r.history, type(r.history))

exit() if not r.status_code == rq.codes.ok else print('Requests Successfully')

files = {
    'file': open('favicon.ico', 'rb')
}
r = rq.post('http://httpbin.org/post', files=files)
print(r.text)

r = rq.get('http://www.baidu.com')
print(r.cookies)

for key, value in r.cookies.items():
    print(key + '=' + value)


headers = {
    'cookie': 'd_c0="AMAme1TYwQ2PTrXhfXVASNyYND64jlyY1Ww=|1529127019"; _zap=c1f8c302-b2fc-4927-8172-3f4846b7a150; _xsrf=D7tKpM4IVesR49F3PRFyzk9OSvH7AkLn; __gads=ID=1e668e70a138419f:T=1540477555:S=ALNI_Mbpoy0puY96E_ALYZoLIgPZ4AtCOw; tst=f; capsion_ticket="2|1:0|10:1550040676|14:capsion_ticket|44:MzhmYzhlMzdmMDlhNGVlMGEwNDk5ZDViMTgyOTM1ZDY=|3db79f51ce58b47a241689061ae732cb1095d1fa77a2d4c149c58804f885a04c"; z_c0="2|1:0|10:1550040680|4:z_c0|92:Mi4xS3N4NEJRQUFBQUFBd0NaN1ZOakJEU1lBQUFCZ0FsVk5hQXhSWFFCWGwxWkNMRWtuOWZVZldkSjZPR0lBV2gtVk1n|1bbeb95fb402546099127a6c50fba6bdfe9a64872c8b3d6419f5a155f768b434"; __utmv=51854390.100-1|2=registration_date=20170719=1^3=entry_date=20170719=1; q_c1=a449c4cf1e024296b4576f1faef68c62|1550758437000|1529127019000; __utma=51854390.541080221.1549600867.1551091941.1551278648.16; __utmz=51854390.1551278648.16.16.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/hsm-7-44/activities; tgw_l7_route=025a67177706b199591bd562de56e55b',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = rq.get("https://www.zhihu.com", headers=headers)
print(r.cookies)
print(r.text)


s = rq.Session()
s.get('http://httpbin.org/cookies/set/number/123546789')
r = s.get('http://httpbin.org/cookies')
print(r.text)

response = rq.get('https://www.12306.cn', verify=False)
print(response.status_code)

r = rq.get("https://www.taobao.com", timeout=1)
print(r.status_code)

url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
