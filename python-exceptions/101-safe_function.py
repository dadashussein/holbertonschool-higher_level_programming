#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = 0
    try:
        if args:
           result = fct(*args)
        else:
            result = fct()
    except ZeroDivisionError as e:
        result = None
        print("Exception: ", e, file=sys.stderr)
    except IndexError as e:
        result = None
        print("Exception: ", e,  file=sys.stderr)
    return result
