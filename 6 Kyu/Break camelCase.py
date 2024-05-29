Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

def solution(s):
    break_Camel = ''
    for i in s:
        if i.isupper():
            break_Camel += ' ' + i
        else:
            break_Camel += i
    return break_Camel
