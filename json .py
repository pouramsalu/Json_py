# # some JSON:
# import json
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["name"])

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

# import json
# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y) 


# # dump:convert python data to json string
# import json
# a={"name":"salu",
# "class":1,
# "age":4
# }
# my_file=open("ques2.json","w")
# json.dump(a,my_file,indent=4)
# my_file.close()

# import json
# dict={"name":"salu",
# "age":2,
# "topic":"python"
# }
# string=json.dumps(dict)
# print(string)
# # print(type(string))
