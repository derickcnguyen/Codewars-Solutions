Task
Given a list of digits, return the smallest number that could be formed from these digits, using the digits only once (ignore duplicates).

def min_value(digits):
    return int(''.join(map(str,sorted(set(digits)))))
