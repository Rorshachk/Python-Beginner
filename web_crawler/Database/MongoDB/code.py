import pymongo


client = pymongo.MongoClient(host='localhost', port=27017)

# db = client.test
db = client['test']
# collection = db.students
collection = db['students']
result = collection.remove()


student3 = {
    'id': '20170303',
    'name': 'Tom',
    'age': 19,
    'gender': 'male'
}
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
result = collection.insert_one(student3)
print(result)
print(result.inserted_id)
result = collection.insert_many([student1, student2])
print(result)
print(result.inserted_ids)
print('')
result = collection.find_one({'gender': 'male'})
print(type(result))
print(result)
print('')

results = collection.find({'gender': 'male'})
print(results)
print(results.count())
print('')
for result in results:
    print(result)

results = collection.find().sort('name', pymongo.ASCENDING)
print(results)
for result in results:
    print(result)


results = collection.find({'name': {'$regex': '^M.*'}})
print(results)
for result in results:
    print(result)

results = collection.find()
print(results.count())
results = results.skip(2)
for result in results:
    print(result)

condition = {'name': 'Mike'}
student = collection.find_one(condition)
student['age'] = 25

# 整个字段替换
result = collection.update(condition, student)
# 只更新student里存在的字段
# result = collecntion.update(condition, {'$set': student})

print(result)
print('')
results = collection.find()
for result in results:
    print(result)


condition = {'name': 'Tom'}
student = collection.find_one(condition)
student['age'] = 19
result = collection.update_one(condition, {'$set': student})
print(result)
print(result.matched_count, result.modified_count)

condition = {'age': {'$gte': 20}}
result = collection.update_many(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)
