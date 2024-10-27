salary = int(input("Enter the salary: "))
if salary <= 4000:
    hra = salary*0.1
    da = salary*0.5
    print(f"The Gross salary is {salary+hra+da}")
elif salary > 4000 and salary<= 8000:
    hra = salary*0.15
    da = salary*0.6
    print(f"The Gross salary is {salary+hra+da}")
elif salary > 8000 and salary<= 12000:
    hra = salary*0.2
    da = salary*0.7
    print(f"The Gross salary is {salary+hra+da}")
elif salary> 12000:
    hra = salary*0.25
    da = salary*0.8
    print(f"The Gross salary is {salary+hra+da}")