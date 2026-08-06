def calculate_salery(hours,price,bonus):
    salery=(hours*price)+bonus    
    return salery
result=calculate_salery(120,500,150)
print(result)