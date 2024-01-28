#!/usr/bin/python3
def multiple_returns(sentence):
    tup = len(sentence), sentence[0] if sentence else None
    return tup
