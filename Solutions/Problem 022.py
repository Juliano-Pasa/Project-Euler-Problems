# https://projecteuler.net/problem=22

import os

def ReadEntry(path):
    with open(path) as f:
        data = f.read().replace("\"", "").split(",")

    return data

def GetNumericValue(name):
    total = 0
    
    for c in name:
        total += ord(c) - 64

    return total

if __name__ == "__main__":
    path = os.path.dirname(__file__) + "\..\Problems Entries\Problem 022 entry.txt"
    data = ReadEntry(path)
    data.sort()
    data = [GetNumericValue(name) for name in data]
    result = sum([(index+1) * value for index, value in enumerate(data)])
    print(result)
