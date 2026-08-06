def show_numbers():
    for i in range(7):
     if i==3:
        continue
     print(i)



def show_numbers2():
   for j in range(7):
      if j==4:
        break
      print(j)

show_numbers()
print("=================")
show_numbers2()
