import math
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
root1=(-b+((b*b-4*a*c)**0.5))/(2*a)
root2=(-b-((b*b-4*a*c)**0.5))/(2*a)
print(f'Root 1 is {root1}')
print(f'Root 2 is {root2}')