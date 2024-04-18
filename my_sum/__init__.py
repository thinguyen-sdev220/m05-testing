# Function called sum(), which takes an iterable (a list, tuple, or set) and adds the values together

def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total