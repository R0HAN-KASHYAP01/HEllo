decimal_number = int(input("Enter the number: "))

binary_number = bin(decimal_number)
octal_number = oct(decimal_number)
hexa_number = hex(decimal_number)

print(f"The binary number of {decimal_number} is {binary_number[2:]}")
print(f"The ocatal number of {decimal_number} is {octal_number[2:]}")
print(f"The Hexa-decimal of {decimal_number} is {hexa_number[2:].upper()} ")


