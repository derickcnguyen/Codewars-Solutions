Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

def xo(s):
    count1 = 0
    count2 = 0
    s = s.lower()
    
    for i,e in enumerate(s):
        if e == 'x':
            count1+=1
        if e == 'o':
            count2+=1
    return count1 == count2
