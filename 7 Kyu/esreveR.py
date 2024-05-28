Write a function reverse which reverses a list (or in clojure's case, any list-like data structure)

(the dedicated builtin(s) functionalities are deactivated)

def reverse(lst):
    empty_list = list()
    for i in lst:
        empty_list.insert(0,i)
    return empty_list
