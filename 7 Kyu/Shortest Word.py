Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

def find_short(s):
    words = s.split()
    shortest_length = len(words[0])
    for word in words:
        shortest_length = min(shortest_length, len(word))
    return shortest_length
