class Shape:
    def setValue(self,side):
        self.side = side
    
class Square(Shape):
    def area(self):
        return self.side**2

class cube(Shape):
    def volume(self):
        return self.side**3


square = Square()
s = int(input("Enter the side of square: "))
square.setValue(s)
print(f"The area of square of side {s} is {square.area()}")

Cube = cube()
s = int(input("Enter the side: "))
Cube.setValue(s)
print(f"The volume of cube of side {s} is {Cube.volume()}")

