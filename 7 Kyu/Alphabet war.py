Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.

The left side letters and their power:

 w - 4
 p - 3
 b - 2
 s - 1
The right side letters and their power:

 m - 4
 q - 3
 d - 2
 z - 1
The other letters don't have power and are only victims.

Example
AlphabetWar("z");        //=> Right side wins!
AlphabetWar("zdqmwpbs"); //=> Let's fight again!
AlphabetWar("zzzzs");    //=> Right side wins!
AlphabetWar("wwwwwwz");  //=> Left side wins!

def alphabet_war(fight):
    d = {'w':4,'p':3,'b':2,'s':1,
        'm':-4,'q':-3,'d':-2,'z':-1}
    solution =  sum("zdqm".find(c) - "sbpw".find(c) for c in fight)
    if solution > 0:
        return 'Right side wins!'
    if solution < 0:
        return 'Left side wins!'
    else:
        return "Let's fight again!"
