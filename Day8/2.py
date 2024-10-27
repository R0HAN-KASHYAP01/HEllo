string = input("Enter the string: ")
if string.lower() == string[::-1].lower():
    print(f"{string} is palindrome")
else:
    print(f"{string} is not palindrome")

