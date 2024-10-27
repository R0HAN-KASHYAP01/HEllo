def lst_maker():
    new_list = []
    lst_input = input("Enter the list separated by commas:\n")
    for i in lst_input.split(","):
        new_list.append(i)
    return new_list

tup = tuple(lst_maker())
print(tup)
