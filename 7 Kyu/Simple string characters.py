In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters (everything else), as follows.

The order is: uppercase letters, lowercase letters, numbers and special characters.

"*'&ABCDabcde12345" --> [ 4, 5, 5, 3 ]

def solve(s):
    isUpper = 0
    isLower = 0
    isInt = 0
    isSpecial = 0
    
    for char in s:
        if char.isupper():
            isUpper += 1
        elif char.islower():
            isLower += 1
        elif char.isdigit():
            isInt += 1
        else:
            isSpecial += 1
    
    return [isUpper, isLower, isInt, isSpecial]
