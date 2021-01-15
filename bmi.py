def is_normal_bmi(weight, height):
    """This function recieves an individual's weight and height, then
     calculates and returns their BMI"""
    bmi = float(weight)/(float(height)**2)
    if bmi<=24.9 and bmi>=18.5:
        return True
    else:
        return False
