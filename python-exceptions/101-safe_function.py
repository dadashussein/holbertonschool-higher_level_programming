#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = 0
    try:
        result = fct(args[0], args[1])
    except ZeroDivisionError as e:
        result = None
        print("Exception: ", e, file=sys.stderr)
    except IndexError as e:
        result = None
        print("Exception: ", e,  file=sys.stderr)
    return result
