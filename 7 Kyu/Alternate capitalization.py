Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

def capitalize(s):
    s = ''.join(c if i % 2 == 0 else c.upper() for i,c in enumerate(s))
    return [s.swapcase(), s]
