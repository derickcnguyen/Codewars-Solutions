Task
Given an array/list [] of integers , Find the product of the k maximal numbers.

Notes
Array/list size is at least 3 .

Array/list's numbers Will be mixture of positives , negatives and zeros

Repetition of numbers in the array/list could occur.

def max_product(lst, n_largest_elements):
    reverse_sorted = sorted(lst, reverse = True)
    largest_elements = reverse_sorted[:n_largest_elements]
    solution = 1
    for i in largest_elements:
        solution *= i
    return solution
