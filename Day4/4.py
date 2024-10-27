def substr(string,substring):
    if substring in string:
        return True
    else:
        return False

string = input("Enter the string: ")
substring = input("Enter the substring: ")

if substr(string,substring):
    print(f"{substring} is present in {string}")

else:
    print(f"{substring} is not present in {string}")

    