x={"name":"gandom","last name":"akbari","age":"20"}
print(x["name"])
print(x["last name"])
y={"1":"gandom","2":"akbari"}
c={"3":"wild","4":"cat"}
y.update(c)
print("y=",y)
print("c=",c)
v=y|c
print(v)
b=[[1,"eli"],[2,"nazi"],[3,"hesam"]]
h=dict(b)
print(h)
e={"name":["ali","gandom","elina"],
   "age":[15,25,98],
   "city":["tehran","tabriz","yazd"]}
m1=e["name"]
m2=e["age"]
m3=e["city"]
n=m1.index("gandom")
m1.pop(n)
m2.pop(n)
m3.pop(n)
e["name"]=m1
e["age"]=m2
e["city"]=m3
print(e)


e={"name":["ali","gandom","elina"],
   "age":[15,25,98],
   "city":["tehran","tabriz","yazd"]}
m1=e["name"]
m2=e["age"]
m3=e["city"]
n=m1.index("gandom")
m1.insert(n+1,"hamta")
m2.insert(n+1,45)
m3.insert(n+1,"rasht")
e["name"]=m1
e["age"]=m2
e["city"]=m3
print(e)
print(e.keys())
print(e.items())