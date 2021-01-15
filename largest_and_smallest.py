def largest_and_smallest(num1, num2, num3):
    """This function receives three numbers and returns the largest
     and smalllest ones out of the three"""
    if num1>num2:
        if num1<=num3:
            return num3, num2
        elif num2<=num3:
            return num1, num2
        else:
            return num1, num3
    elif num1>=num3:
        return num2, num3
    else:
        if num2>=num3:
            return num2, num1
        else:
            return num3, num1
