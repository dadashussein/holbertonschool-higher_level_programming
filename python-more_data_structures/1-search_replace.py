#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced = []
    for i in my_list:
        replaced.append(replace if i == search else i)
    return replaced
