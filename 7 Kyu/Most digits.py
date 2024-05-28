Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array.

def find_longest(arr):
    most_digits = 0
    longest_number = 0
    
    for i in arr:
        curr_digits = len(str(i))
        if curr_digits > most_digits:
            most_digits = curr_digits
            longest_number = i
    return longest_number
