A number is a Special Number if it’s digits only consist 0, 1, 2, 3, 4 or 5

Given a number determine if it special number or not .

def special_number(number):
    num_to_str = str(number)
    special_digits = {'0', '1', '2', '3', '4', '5'}
    
    for i in num_to_str:
        if i not in special_digits:
            return "NOT!!"
    
    return "Special!!"
