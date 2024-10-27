num = int(input("Enter the number: "))
orginal_num = num
armstong = 0
while(num!= 0):
    digit = num %10
    armstong += digit**3
    num = num// 10

if armstong == orginal_num:
    print(f"The number {orginal_num} is a Armstrong number")
else:
    print(f"The number {orginal_num} is not a Armstrong number")
