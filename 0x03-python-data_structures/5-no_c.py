#!/usr/bin/python3

def no_c(my_string):

    copy_string = [k for k in my_string if k != 'c' and k != 'C']
    return ("".join(copy_string))
