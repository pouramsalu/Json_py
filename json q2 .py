import json

samplejson={"key1":"value1","key2":"value2","key3":"value3"}
# samplejson={"key3":"value3"}
file=open("pen.json","w")
json.dump(samplejson,file,indent=4)
file.close()