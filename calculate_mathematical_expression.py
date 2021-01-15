def calculate_mathematical_expression(num1, num2, mathematical_operator):
    """This function receives two numbers and a mathematical operator and
    calculates the result of the numbers, applied by the operator"""
    num1=float(num1)
    num2=float(num2)
    if mathematical_operator=="+":
        return num1+num2
    elif mathematical_operator=="-":
        return num1-num2
    elif mathematical_operator=="*":
        return num1*num2
    elif mathematical_operator=="/":
        if num2!=0:
            return num1/num2
        else:
            return None
    else:
        return None

def calculate_from_string(math_text):
    """This function receives a text message containing a methematical expression and returns its calculation"""
    #math_text must be built as a string in the following order: number, space, operator, space, number.
    x=math_text.split(" ")
    return calculate_mathematical_expression((x[0]), (x[2]), x[1])
