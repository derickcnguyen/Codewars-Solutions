Disarium number is the number that The sum of its digits powered with their respective positions is equal to the number itself.

Task
Given a number, Find if it is Disarium or not .

Warm-up (Highly recommended)
Playing With Numbers Series
Notes
Number passed is always Positive .
Return the result as String
Input >> Output Examples
disariumNumber(89) ==> return "Disarium !!"

def disarium_number(number):
    disarium = sum(int(e) ** (i + 1) for i, e in enumerate(str(number)))
    return "Disarium !!" if disarium == number else "Not !!"
