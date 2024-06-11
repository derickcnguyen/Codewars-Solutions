Write function alternateCase which switch every letter in string from upper to lower and from lower to upper. E.g: Hello World -> hELLO wORLD

def alternate_case(s):
    reversed = ''
    for i in s:
        if i == i.upper():
            reversed += i.lower()
        else:
            reversed += i.upper()
    return reversed
