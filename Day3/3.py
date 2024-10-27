AR = eval(input("Enter the list of numbers:-\n"))
EAR = []
OAR = []
for num in AR:
    if num%2 == 0:
        EAR.append(num)
    else:
        OAR.append(num)

print(f"The even numbers in the list are:-\n {EAR}")
print(f"The odd numbers in the list are:-\n {OAR}")

