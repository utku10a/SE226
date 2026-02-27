import math

x1=float(input("Enter first point's x coordinate:"));
y1=float(input("Enter first point's y coordinate:"));
x2=float(input("Enter second point's x coordinate:"));
y2=float(input("Enter second point's y coordinate:"));

mesafe = math.sqrt((x2 - x1)**2 + (y2 - y1)**2);
print(f"Distance between these points is: {mesafe}");
