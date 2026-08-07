def matris(a,b):
    c=[[0,0,0],[0,0,0]]
    for i in range (len(a)):
        for j in range(len(a[0])):
            c[i][j]=a[i][j]+b[i][j]



    return(c)
a=[[1,2,-3],
   [0,-1,1]]

b=[[0,-1,2],
   [-1,3,-2]]
result=matris(a,b)
print(result)