import json
import csv

data = []
writing = []
with open('data.json', 'r', encoding='utf-8') as file:
    str = file.read()
    data = json.loads(str)

print(data)

print(data[0])
print(type(data[0]))
with open('data.csv', 'w', encoding='utf-8') as c_file:
    for key, value in data[0].items():
        writing.append(key)
    writer = csv.writer(c_file)
    writer.writerow(writing)
    for movie in data:
        writing.clear()
        for key, value in movie.items():
            writing.append(value)
        writer.writerow(writing)
