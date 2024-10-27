try:
    num1 = int(input("Enter the number: "))
    num2 = int(input("Enter the number: "))
    result = num1/num2
    print(f"Result of division is {result}")

except ValueError:
    print("Error: please Enter a valid number!!")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")