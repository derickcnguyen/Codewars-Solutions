Your task is to return a number from a string.

Details
You will be given a string of numbers and letters mixed up, you have to return all the numbers in that string in the order they occur.

def filter_string(st):
    number = ''
    for char in st:
        if char.isdigit():
            number += char
    return int(number)

or

def filter_string(st):
    return int(''.join(i for i in st if i.isdigit()))
