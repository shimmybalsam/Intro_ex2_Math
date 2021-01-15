def quadratic_equation(num1, num2, num3):
    """This function recieves the coefficients of a quadratic equation and
     returns the results of the equation"""
    a=float(num1)
    b=float(num2)
    c=float(num3)
    if int(a)==0 or (b**2-(4*a*c))<0:
        return None, None
    else:
        complex_route=(b**2-(4*a*c))**0.5
        x1=(-b+complex_route)/(2*a)
        x2=(-b-complex_route)/(2*a)
        if x1==x2:
            return x1, None
        else:
            return x1, x2

def quadratic_equation_user_input():
    """This functions interactively receives the coefficients of a quadratic equation
     and prints out the results of the equation, using the former quadric equation function"""
    a1, b1, c1 = (input("Insert coefficients a, b, and c: ")).split()
    x, y = quadratic_equation(a1, b1, c1)
    if x!=None:
        if y!=None:
            print("The equation has 2 solutions: " + str(x) + " and " + str(y))
        else:
            print ("The equation has 1 solution: " + str(x))
    elif y!=None:
        print("The equation has 1 solution: " + str(y))
    else:
        print ("The equation has no solutions")




