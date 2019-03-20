import json

file_name = 'data.json'
with open(file_name, encoding='utf-8') as f_obj:
    data = json.load(f_obj)
    items = data.get('data').get('cards')
#    print(items[0])
    print(items[0].get('mblog'))
    print(items[0].get('id'))
