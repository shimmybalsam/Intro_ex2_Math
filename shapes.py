import math

def circle_area(radius):
    """Calculates the area of a circle"""
    return (math.pi*radius*radius)

def rect_area(side1, side2):
    """Calculates the area of a rectangle"""
    return side1*side2

def trap_area(base1, base2, height):
    """calculates the area of a trapezoid"""
    return ((base1+base2)*height)/2

def shape_area():
    """This function interactively recieves the data of a specific geometrical
     shape and returns the area of said shape"""
    shape=input("Choose shape (1=circle, 2=rectangle, 3=trapezoid): ")
    if shape != "1" and shape != "2" and shape != "3":
        return None
    elif shape == "1":
        r= float(input())
        return circle_area(r)
    elif shape == "2":
        x = float(input())
        y = float(input())
        return rect_area(x, y)
    else:
        a = float(input())
        b = float(input())
        h = float(input())
        return trap_area(a, b, h)
