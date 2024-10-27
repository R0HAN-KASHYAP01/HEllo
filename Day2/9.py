num = int(input("Enter the number: "))
sum = 0
original_num = num
while(num!=0):
    digit = num%10
    sum = sum + digit
    num = num // 10

print(f"The sum of digit of {original_num} is {sum}")
