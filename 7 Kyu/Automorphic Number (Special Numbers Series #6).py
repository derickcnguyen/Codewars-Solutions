A number is called Automorphic number if and only if its square ends in the same digits as the number itself.

Task
Given a number determine if it Automorphic or not .

def automorphic(num):
    square = num ** 2
    if str(square).endswith(str(num)):
        return 'Automorphic'
    else:
        return 'Not!!'
