string = input("Enter the string: ")
count = 0
for ch in string:
    if ch.isnumeric():
        count += 1
    
print(f"The number of digits present are {count}")
