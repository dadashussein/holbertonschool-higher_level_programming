#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = 0
    try:
        if args:
            result = fct(*args)
        else:
            result = fct()
    except (ZeroDivisionError, IndexError) as e:
        print("Exception: ", e, file=sys.stderr)
        result = None
    return result
