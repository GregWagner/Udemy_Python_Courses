def string_length(s):
    if type(s) == int:
        return "Sorry, ints do not have a length"
    elif type(s) == float:
        return "Sorry, floats do not have a length"
    else:
        return len(s)
