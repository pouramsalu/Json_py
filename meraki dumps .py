import json

# a={"lalalala": 3}
# mystring = json.dumps(a)
# print(mystring)

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"]) 