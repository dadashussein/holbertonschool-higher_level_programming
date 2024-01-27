#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_array = my_list.copy()
    if idx < 0:
        return new_array
    if idx >= len(my_list):
        new_array
    new_array[idx] = element
    return new_array
