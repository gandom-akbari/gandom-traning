def extract_even(x):  
    r=[]  
    for i in range(x): 
         if i%2==0:
          r.append(i)   

    return(r)

if __name__ == "__main__":
 x=101
 result=extract_even(x)

 print(result)