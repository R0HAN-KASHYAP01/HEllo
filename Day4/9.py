import tempconv

temp = eval(input("Enter the temperature: "))

print(f"{temp} celsius in fahrenheit is {tempconv.ctof(temp)}")
print(f"{temp} fahrenheit in celsius is {tempconv.ftoc(temp)}")
