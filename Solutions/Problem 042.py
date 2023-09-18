import os
import csv

def WordToValue(word):
    soma = 0
    for c in word:
        soma += ord(c) - ord('A') + 1
    return soma

def readEntry(path):
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = []
        
        for row in reader:
            data += row
        
        return [*map(WordToValue, data)]

def GenerateTriangles(n):
    result = [1]
    for i in range(2, n+1):
        result.append(result[-1] + i)
    return set(result)

def CountTriangleWords(data, triangles):
    count = 0

    for n in data:
        if n in triangles:
            count += 1

    return count

if __name__ == "__main__":
    path = os.path.dirname(__file__) + "\..\Problems Entries\Problem 042 entry.txt"
    data = readEntry(path)
    triangles = GenerateTriangles(max(data))
    result =  CountTriangleWords(data, triangles)
    print(result)