Given a mixed array of number and string representations of integers, add up the non-string integers and subtract the total of the string integers.

Return as a number.

def div_con(x):
    integs = 0
    strs = 0
    
    for i in x:
        if isinstance(i, int):
            integs += i
        elif isinstance(i, str) and i.isdigit():
            strs += int(i)
    return integs - strs
