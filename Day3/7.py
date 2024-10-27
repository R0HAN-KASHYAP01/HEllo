def Set_maker():
    new_set = set()
    set_input = input("Enter the list separated by commas:-\n")
    for i in set_input.split(","):
        new_set.add(i)
    return new_set

s = Set_maker()
for i in s:
    print(i)
    