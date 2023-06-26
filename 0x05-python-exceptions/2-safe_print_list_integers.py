#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    sum_of_elements = 0
    for p in range(x):
        try:
            print("{:d}".format(my_list[p]), end="")
            sum_of_elements += 1
        except (TypeError, ValueError):
            continue
    print("")
    return sum_of_elements
