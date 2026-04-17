import geometry_utils as gu

print("Shapes you can use: circle / rectangle / triangle")
print("Operations: _area or _perimeter (example: circle_area)")

op = input("Choose an operation: ")

if op == "circle_area":
    r = float(input("Radius value: "))
    result = gu.circle_area(r)

elif op == "circle_perimeter":
    r = float(input("Radius value: "))
    result = gu.circle_perimeter(r)

elif op == "rectangle_area":
    w = float(input("Width: "))
    h = float(input("Height: "))
    result = gu.rectangle_area(w, h)

elif op == "rectangle_perimeter":
    w = float(input("Width: "))
    h = float(input("Height: "))
    result = gu.rectangle_perimeter(w, h)

elif op == "triangle_area":
    b = float(input("Base length: "))
    h = float(input("Height: "))
    result = gu.triangle_area(b, h)

else:
    result = "Unknown operation."

print("Output:", result)