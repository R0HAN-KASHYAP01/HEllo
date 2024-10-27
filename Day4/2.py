def calc():
    num1 = int(input("Enter the number: "))
    num2 = int(input("Enter the number: "))
    sum = num1+num2
    sub = num1-num2
    mul = num1*num2
    div = num1 / num2
    result = [sum,sub,mul,div]
    return result

lst = calc()
print(lst)
