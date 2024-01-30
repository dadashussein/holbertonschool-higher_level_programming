#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for key in a_dictionary:
        value = a_dictionary[key] * 2
        new_dic[key] = value
    return new_dic
