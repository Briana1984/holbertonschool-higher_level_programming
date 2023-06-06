#!/usr/bin/python3
def multiple_returns(sentence):
    tple = []
    if not sentence:
        tple = len(sentence), None
        return tple
    else:
        tple = len(sentence), sentence[0]
        return (tple)