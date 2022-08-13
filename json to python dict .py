# import json
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(y["age"]) 

# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None)) 

import json
json_obj = '{ "Name":"David", "Class":"I", "Age":6 }'
python_obj = json.loads(json_obj)
print("JSON data: {}".format(python_obj))
for key in python_obj:
    print("{}: {} ".format(key, python_obj[key]))