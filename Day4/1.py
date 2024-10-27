def area(l,b):
    print(f"Area of rectangle of length {l} and breadth {b} is {l*b}")

def peri(l,b):
    print(f"Perimeter of rectangle of length {l} and breadth {b} is {2*(l+b)}")

length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
area(length,breadth)
peri(length,breadth)
