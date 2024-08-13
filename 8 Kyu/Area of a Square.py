Complete the function that calculates the area of the red square, when the length of the circular arc A is given as the input. Return the result rounded to two decimals.

Graph

Note: use the π value provided in your language (Math::PI, M_PI, math.pi, etc)

import math
pi = math.pi
def square_area(A):
    circle = 4 * A
    pi = math.pi
    return round((circle  / (2 * pi)) ** 2,2)
