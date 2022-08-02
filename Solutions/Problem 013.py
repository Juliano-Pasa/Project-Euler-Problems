# https://projecteuler.net/problem=13


import csv

def readEntry(path):
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = []
        
        for row in reader:
            row = [int(val) for val in row[:-1]]
            data.append(row[0])
    
    return data

def sumLastDecimalPlace(numbers, carry):
    totalSum = carry

    for num in numbers:
        totalSum += num % 10

    lastDigit = totalSum % 10
    nextCarry = int(totalSum//10)

    return lastDigit, nextCarry

if __name__ == "__main__":
    data = readEntry("path")
    last10Digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    j = 0
    carry = 0

    while carry != 0 or max(data) != 0:
        lastDigit, carry = sumLastDecimalPlace(data, carry)
        last10Digits[j] = lastDigit
        j = (j + 1) % 10

        data = list(map(lambda x : int(x//10), data))

    last10Digits = list(reversed(last10Digits))
    size = len(last10Digits)
    aux = []
    for i in range(size):
        aux.append(last10Digits[(size-j + i) % 10])

    print(aux)