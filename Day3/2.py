lst = eval(input("Enter the numbers:-\n"))
search = int(input("Enter the number to search: "))
for num in lst:
    if num == search:
        print(f"{search} is presented in list")
        break

    elif num == lst[len(lst)-1] and num != search:
        print(f"{search} is not presented in list")

 