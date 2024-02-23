Write a function that accepts two integers and returns the remainder of dividing the larger value by the smaller value.

Division by zero should return an empty value.

def remainder(a,b):
    numerator = max(a,b)
    denominator = min(a,b)
    
    if denominator == 0:
        return None
    
    return numerator % denominator
