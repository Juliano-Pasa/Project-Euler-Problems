# https://projecteuler.net/problem=11


import math
import csv

def readEntry(path):
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = []
        size = 0
        
        for row in reader:
            row = [int(val) for val in row[:-1]]
            data += row
            size = len(row)

        return data, size

def calculateProduct(entry):
    return math.prod(entry)

def findGreatest4Product(row):
    greatestProduct = -1
    if (len(row) < 4):
        return -1

    for i in range(len(row) - 3):
        product = calculateProduct(row[i:i+4])
        greatestProduct = product if product > greatestProduct else greatestProduct

    return greatestProduct

if __name__ == "__main__":
    data, size = readEntry("path")
    greatestProduct = -1
    products = [0, 0, 0, 0, 0, 0]

    for i in range(size):
        products[0] = findGreatest4Product(data[size*i: size*i + size]) # rows
        products[1] = findGreatest4Product(data[i::size]) # cols
        products[2] = findGreatest4Product(data[i::size+1]) # upperLeftTriangle
        products[3] = findGreatest4Product(data[size-1-i::size-1]) # upperRightTriangle
        products[4] = findGreatest4Product(data[size*(i+1)::size+1]) # lowerLeftTriangle
        products[5] = findGreatest4Product(data[size-1-i + size*(i+1)::size-1]) # lowerRightTriangle

        product = max(products)
        greatestProduct = product if product > greatestProduct else greatestProduct

    print(greatestProduct)
