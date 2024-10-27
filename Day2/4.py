X = float(input("Enter the x-coordinate: "))
Y = float(input("Enter the y-coordinate: "))

if X > 0 and Y > 0:
    print(f"({X:.2f},{Y:.2f}) is present in the First Quadrant")
elif X < 0 and Y > 0:
    print(f"({X:.2f},{Y:.2f}) is present in the Second Quadrant")
elif X < 0 and Y < 0:
    print(f"({X:.2f},{Y:.2f}) is present in the Third Quadrant")
elif X > 0 and Y < 0:
    print(f"({X:.2f},{Y:.2f}) is present in the Fourth Quadrant")
elif X == 0 and Y == 0:
    print(f"({X:.2f},{Y:.2f}) is at the Origin")
elif X == 0:
    print(f"({X:.2f},{Y:.2f}) lies on the Y-axis")
elif Y == 0:
    print(f"({X:.2f},{Y:.2f}) lies on the X-axis")
