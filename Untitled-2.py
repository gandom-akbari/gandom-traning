x=["gandom","ali","elina","reza","maryam","maede"]
x.append("baran")
print(x)

x=["gandom","ali","elina","reza","maryam","maede"]
x.extend(["bahar","mohamad"])
print(x)

x=["gandom","ali","elina","reza","maryam","maede"]
x.insert(3,"neda")
print(x)

x=["gandom","ali","elina","reza","maryam","maede"]
x.remove("gandom")
print(x)

x=["gandom","ali","elina","reza","maryam","maede"]
x.pop(3)
print(x)

x=["gandom","ali","elina","reza","maryam","maede"]
x.clear()
print(x)
x=["gandom","ali","elina","reza","maryam","maede"]
del x
print(x)


x=["gandom",10,"ali",10,"elina","reza",10,"maryam","maede"]
n=x.count(10)
for i in range(n):
    x.remove(10)

print(x)    



x=["moon","sun",[-15,"stars"],"books","me"]
print(x[2])