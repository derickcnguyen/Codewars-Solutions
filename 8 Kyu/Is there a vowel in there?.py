Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).

If they are, change the array value to a string of that vowel.

Return the resulting array.

def is_vow(arr):
    vowels = {'a','e','i','o','u'}
    for i in range(len(arr)):
        if chr(arr[i]) in vowels:
            arr[i] = chr(arr[i])
    return arr
