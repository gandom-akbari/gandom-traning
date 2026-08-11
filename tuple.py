
x=(2,-8,"gandom",[1,2,3],("ali",4),2,2)
print(len(x))
print(type(x))
print(x[2])
print(x[-1])

y=(1,"alice")
z=x+y
print(z)
n=x.index(-8)
print(n)
m=x.count(2)
print(m)
x=list(x)
print(x)
nn=x.index("gandom")
x.insert(nn+1,88)
print(x)
x=tuple(x)
print(x)
for i in x:
    print("i=",i)

    p=((2,12),(3,13),(4,14))
    for i,j in p:
        print("i=",i)
        print("j=",j)
        print("========================")