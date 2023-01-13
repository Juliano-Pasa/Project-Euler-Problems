# https://projecteuler.net/problem=15


import time

def generatePascalLine(num):
    line = [1]
    currentTerm = 1
    last = 1
    i = num - 1

    while i != 0:
        next = last * (num - currentTerm) // currentTerm
        line.append(next)
        last = next
        currentTerm += 1
        i -= 1

    return line

def calculateLatticePaths(dim):
    line = dim*2 + 1
    pascalLine = generatePascalLine(line)

    return max(pascalLine)

if __name__ == "__main__":
    start = time.time()
    result = calculateLatticePaths(20)
    duration = time.time() - start

    print(result, duration)