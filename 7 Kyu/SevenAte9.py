Write a function that removes every lone 9 that is inbetween 7s.

"79712312" --> "7712312"
"79797"    --> "777"

def seven_ate9(s):
    while '797' in s:
        s = s.replace('797','77')
    return s
