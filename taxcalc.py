salary=int(input("enter salary"))

if salary>12500:
    taxpay=salary-12500
    tax=taxpay*0.8
    netsalary=12500+tax
if salary<12500:
    netsalary=salary
    
print(netsalary)