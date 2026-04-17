PI = 3.14
er = "Dimensions must be positive."
def circle_area(radius):
    if radius <= 0:
        return er
    return PI * radius * radius

def circle_perimeter(radius):
    if radius <= 0:
        return er
    return 2 * PI * radius

def rectangle_area(width, height):
    if width <= 0 or height <= 0:
        return er
    return width * height

def rectangle_perimeter(width, height):
    if width <= 0 or height <= 0:
        return er
    return 2 * (width + height)

def triangle_area(base, height):
    if base <= 0 or height <= 0:
        return er
    return (base * height) / 2