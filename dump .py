# dump:convert python data to json 
# import json
# a={"name":"salu",
# "class":1,
# "age":4
# }
# my_file=open("ques2.json","w")
# json.dump(a,my_file,indent=4)
# my_file.close()

# import json
# a={
#     "name": "David", 
#     "class": "I", 
#     "age": 6
# }
# f=open("salu2.json","w")
# json.dump(a,f,indent=3)
# f.close()

# import json
# a={"key1":"value1","key2":"value2"}
# f=open("dict.json","w")
# json.dump(a,f,indent=3)
# f.close()


import json
dict={"id":1,"name":"value2","age":29}
file=open("devika.json","w")
json.dump(dict,file,indent=3)
file.close()
