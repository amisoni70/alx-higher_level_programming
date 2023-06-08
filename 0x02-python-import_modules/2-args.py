#!/usr/bin/python3
import sys

if __name__ == "__main__":
    Str = "{:d} argument"
    count = len(sys.argv) - 1
    if count == 0:
        Str += 's.'
    elif count == 1:
        Str += ':'
    else:
        Str += 's:'
    print(Str.format(count))

    p = 0
    for arg in sys.argv:
        if p != 0:
            print("{:d}: {:s}".format(p, arg))
        p += 1
