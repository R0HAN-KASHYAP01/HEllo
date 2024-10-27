tupl = (1,2,0,8,4,5)
def len(tup):
    length = 0
    for i in tup:
        length += 1
    return length

def max(tup):
    max_num = 0
    for i in tup:
        if i > max_num:
            max_num = i

    return max_num

def min(tup):
    min_num = tup[0]
    for i in tup:
        if i < min_num:
            min_num = i
    
    return min_num

def sum(tup):
    result = 0
    for i in tup:
        result += i
    
    return result

print(f"The length of tuple is {len(tupl)}")
print(f"The maximum number of tuple is {max(tupl)}")
print(f"The minimum number of tuple is {min(tupl)}")
print(f"The sum of number of tuple is {sum(tupl)}")

