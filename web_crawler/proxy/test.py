import requests

# 设置代理地址

proxies = {
    'http': 'http://' + '62.4.60.50:53281'
}

# 然后剩下的就跟正常使用差不多，只不过此时的request已经是绑定了代理之后的request
url = 'https://weixin.sogou.com/weixin?query=NBA&type=2&page=1'
response = requests.get(url, allow_redirects=False, proxies=proxies)
if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)
