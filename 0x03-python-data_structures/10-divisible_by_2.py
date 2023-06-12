#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    two = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            two.append(True)
        else:
            two.append(False)
    return(two)
