# https://projecteuler.net/problem=18


import csv
import os

def readEntry(path):
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=" ")
        data = []

        for line in reader:
            row = [int(value) for value in line]
            data.append(row)

    return data

def calculateMaxPathSum(data):
    i = len(data) - 2
    j = 0

    while i >= 0:
        j = 0
        rowSize = len(data[i])
        while j < rowSize:           
            data[i][j] += max(data[i+1][j:j+2])
            j += 1
        i -= 1
    
    return data[0][0]

if __name__ == "__main__":
    path = os.path.dirname(__file__) + "\..\Problems Entries\Problem 018 entry.txt"
    data = readEntry(path)
    result = calculateMaxPathSum(data)
    print(result)