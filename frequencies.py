"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in range(len(items)):
        items[i] = str(items[i])
    for k in range(len(items)):
        if items[k] in frequencies:
            frequencies[items[k]] += 1
        else:
            frequencies[items[k]] = 1
    return frequencies
