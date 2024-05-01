Complete the function, which calculates how much you need to tip based on the total amount of the bill and the service.

You need to consider the following ratings:

Terrible: tip 0%
Poor: tip 5%
Good: tip 10%
Great: tip 15%
Excellent: tip 20%
The rating is case insensitive (so "great" = "GREAT"). If an unrecognised rating is received, then you need to return:

"Rating not recognised" in Javascript, Python and Ruby...
...or null in Java
...or -1 in C#
Because you're a nice person, you always round up the tip, regardless of the service.

import math
def calculate_tip(amount, rating):
    rating = rating.lower()
    if rating == 'terrible':
        return 0
    if rating == 'poor':
        return math.ceil(amount * .05)
    if rating == 'good':
        return math.ceil(amount * .1)
    if rating == 'great':
        return math.ceil(amount * .15)
    if rating == 'excellent':
        return math.ceil(amount * .2)
    else:
        return 'Rating not recognised'
