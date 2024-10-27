units = int(input("Enter the Units: "))
if units <= 150:
    print(f"Bill for the {units} units is {units*2.40}")
elif units <= 300:
    print(f"Bill for the {units} units is {(150*2.40)+((units-150)*3.00)}")
elif units > 300:
    print(f"Bill for the {units} units is {(150*2.40)+((units-300)*3.20)+ (300*3.00)}")
