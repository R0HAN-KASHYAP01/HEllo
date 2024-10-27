def lst_maker():
    new_list = []
    lst_input = input("Enter the list separated by commas:\n")
    for i in lst_input.split(","):
        new_list.append(i)
    return new_list

student_name = lst_maker()
student_name = sorted(student_name)
print("The names of student in ascending order:-")
for name in student_name:
    print(name)
print("The names of student in descending ordre:-")
for name in student_name[::-1]:
    print(name)
    
