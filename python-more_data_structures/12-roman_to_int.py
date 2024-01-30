#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    new_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    total = 0
    p_value = 0
    for char in roman_string:
        c_value = new_dict[char]
        if p_value < c_value:
            total -= p_value
        total += c_value
        p_value = c_value
    return total
