def search(lst,num):
    for i in range(len(lst)):
        if lst[i] == num:
            print(f"The number {num} is present in list at index {i}")
        

def lst_maker():
    new_list = []
    lst_input = input("Enter the list separated by commas:\n")
    for i in lst_input.split(","):
        new_list.append(int(i))
    return new_list

num = int(input("Enter the number to be searched: "))
search(lst_maker(),num)
