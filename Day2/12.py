num = int(input("Enter the number: "))
is_prime = True

for i in range(2,int(num**0.5)):
    if num %i == 0:
        is_prime = False
        break

if is_prime:
    print(f"The number {num} is a prime number")

else:
    print(f"The number {num} is not a prime number")

