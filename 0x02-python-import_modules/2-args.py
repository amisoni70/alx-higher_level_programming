#!/usr/bin/python3
import sys

if __name__ == "__main__":
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguements.")
    elif count == 1:
        print("1 arguement.")
    else:
        print("{} arguements:".format(count))
    for p in range(count):
        print("{}:{}".format(p + 1, sys.argv[p + 1]))
