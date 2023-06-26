#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        p = fct(*args)
        return p
    except BaseException as e:
        p = None
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return p
