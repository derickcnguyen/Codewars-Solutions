Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are a part of the word in this kata.

def reverse_alternate(st):
    split_words = st.split()
    for i in range(len(split_words)):
        if i % 2 == 1:
            split_words[i] = split_words[i][::-1]
    return ' '.join(split_words)
