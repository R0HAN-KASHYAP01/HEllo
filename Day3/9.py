key = "a"
dic = {}
while(key != ""):
    key = input("Enter the key: ")
    if key == "":
        break
    Value = input("Enter the value: ")
    dic[key] = Value

print("The key value pairs in dict are:-")

for keys in dic:
    print(f"{keys} : {dic[keys]}")


