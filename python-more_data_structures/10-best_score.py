#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    values_d = sorted(a_dictionary.values())
    best_value = values_d[len(values_d) - 1]
    best_key = 0
    for key in a_dictionary:
        best_key = a_dictionary[key] = best_value
    return best_key
