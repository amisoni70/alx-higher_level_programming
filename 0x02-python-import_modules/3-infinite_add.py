#!/usr/bin/python3
import sys

if __name__ == "__main__":

    count = len(sys.argv) - 1

    p = 0
    total = 0
    for arg in sys.argv:
        if p != 0:
            total += int(arg)
        else:
            p += 1
        print("{:d}".format(total))
