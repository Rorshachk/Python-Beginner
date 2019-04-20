import json
from urllib.parse import quote
with open('in.json') as f:
    cookies = json.load(f)

for cookie in cookies:
    if cookie['secure'] == False:
        cookie['secure'] = 'False'
    else:
        cookie['secure'] = 'True'

    if cookie['httpOnly'] == False:
        cookie['httpOnly'] = 'False'
    else:
        cookie['httpOnly'] = 'True'

    print('{')
    print('name="' + cookie['name'] + '",')
    print('value="' + cookie['value'] + '",')
    print('path="' + cookie['path'] + '",')
    print('domain="' + cookie['domain'] + '",')
    print('secure=' + cookie['secure'] + ',')
    print('httpOnly=' + cookie['httpOnly'] + '},')
