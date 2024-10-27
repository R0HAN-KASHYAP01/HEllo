vowels = "aeiou"
line = input("Enter the string:- ")
occ = 0
for ch in line:
    if ch.lower() in vowels:
        occ += 1

print(f'The number of vowels present in {line} is  {occ}')
