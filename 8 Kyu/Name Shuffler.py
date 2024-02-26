Write a function that returns a string in which firstname is swapped with last name.

Example(Input --> Output)

"john McClane" --> "McClane john"

def name_shuffler(str_):
    str_ = str_.split()
    return str_[1] + ' ' + str_[0]
