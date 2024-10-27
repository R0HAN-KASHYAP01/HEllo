class Figure:
    def area(self,side1,side2=None):
        if side2 == None:
            return side1**2
        else:
            return side1*side2

figure = Figure()
side = int(input("Enter the side of square: "))
print(f"The area of square is {figure.area(side)}")

length = int(input("Enter the length of rectangle: "))
breadth = int(input("Enter the breadth of rectangle: "))
print(f"The area of rectangle is {figure.area(length,breadth)}")
