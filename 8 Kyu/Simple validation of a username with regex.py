Write a simple regex to validate a username. Allowed characters are:

lowercase letters,
numbers,
underscore
Length should be between 4 and 16 characters (both included).

def validate_usr(username):
    if not 4 <= len(username) <= 16:
        return False
    for char in username:
        if not ('a' <= char <= 'z' or '0' <= char <= '9' or char == '_'):
            return False
    return True
