import requests
from operator import itemgetter
import json

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

submission_ids = r.json()
submission_dicts = []
cnt = 0
# print(submission_ids[18])
for submission_id in submission_ids[:30]:
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
           str(submission_id) + '.json')
    submission_r = requests.get(url)
    cnt += 1
    print(str(cnt) + ': ' + str(submission_r.status_code))
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(
    submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("\nDiscussion Link", submission_dict['link'])
    print("comments:", submission_dict['comments'])

filename = 'hn_submissions_save.json'
with open(filename, 'w') as f_obj:
    json.dump(submission_dicts, f_obj)
