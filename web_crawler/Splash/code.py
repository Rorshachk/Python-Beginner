import requests
from urllib.parse import quote


url = 'http://localhost:8050/render.html?url=https://www.baidu.com'
response = requests.get(url)
print(response.text)

'''
url = 'http://localhost:8050/render.png?url=https://www.jd.com&wait=5&width=1000&height=700'
response = requests.get(url)
with open('jd.png', 'wb') as f:
    f.write(response.content)
'''

lua = '''
function main(splash, args)
    local treat = require('treat')
    local response = splash:http_get("http://httpbin.org/get")
      return{
         html = treat.as_string(response.body),
         url = response.url,
         status = response.status
      }
end
'''
url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
print(url)
response = requests.get(url)
print(response.text)
