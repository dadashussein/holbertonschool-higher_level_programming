#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for x in my_string:
        if x.lower() != 'c':
            result += x
    return result
