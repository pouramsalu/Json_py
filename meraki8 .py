# import json
# file="file_dic_to_json.txt"
# c=["Name","Disgnation","age","salary"]
# d={}
# with open(file) as f1:
#     x=1
#     for i in f1:
#         a=list( i.strip().split(None,4))
#         print(a)
#         b="emp"+str(x)
#         j=0
#         dic={}
#         while j<len(c):
#             dic[c[j]]=a[j]
#             j=j+1
#         d[b]=dic   
#         x=x+1
# with open("dic_to_json.json","w") as f:
#     json.dump( d , f , indent=5)

a=["Neelam","programer","24","2400"]
b=["Komal","trainer","24","20000"]
c=["Anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
l=["Name","Designation","Age","Salary"]
d1={}
d2={}
d3={}
d4={}
i=0
while i<len(l):
        x= []    
        d1[l[i]]=a[i]
        d2[l[i]]=b[i]
        d3[l[i]]=c[i]
        d4[l[i]]=d[i]
        x.append(d1)
        x.append(d2)
        x.append(d3)
        x.append(d4)
        i+=1
z=["emp1","emp2","emp3","emp4"]
dic={}
i=0
while i<len(x):
    dic[z[i]]=x[i]
    i+=1
print(dic)
import json
with open("meraki8.json","w") as f:
    json.dump(dic,f,indent=6)