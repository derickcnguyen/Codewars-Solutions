Write function parse_float which takes a string/list and returns a number or 'none' if conversion is not possible.

def parse_float(string):
    try:
        return float(string)
    except (ValueError, TypeError):
        return None
