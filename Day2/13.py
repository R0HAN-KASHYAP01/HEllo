intial = int(input("Enter the Initial value of range: "))
final = int(input("Enter the final value of the range: "))

print(f"The prime number in range ({intial},{final})  are:- ")
for i in range(intial,final+1):
    for j in range(2,i):
        if i % j == 0:
            break
        elif j == i-1:
            print(i)

