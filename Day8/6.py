full_name = input("Enter the full name: ")

short_name = ""

name_parts = full_name.split()

for part in name_parts[:-1]:
    short_name += part[0].upper()+"."

short_name += name_parts[-1].capitalize()

print(f"Short name: {short_name}")
