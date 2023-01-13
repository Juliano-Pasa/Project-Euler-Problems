# https://projecteuler.net/problem=17


import time

def getOnes(value):
    ones = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
    return ones[value]

def getTeens(value):
    teens = {10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
    return teens[value]

def getTens(value):
    tens = {0:0, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}
    return tens[value]

def calculateNumLength(num):
    total = 0
    tensAndOnes = num % 100

    if 9 < tensAndOnes < 20:
        total += getTeens(tensAndOnes)
    else:
        ones = tensAndOnes % 10
        total += getOnes(ones)
        tens = tensAndOnes // 10
        total += getTens(tens)

    hundreds = num // 100
    if hundreds != 0:
        total += getOnes(hundreds)
        total += 10 if tensAndOnes else 7
    
    return total

if __name__ == "__main__":
    start = time.time()
    total = 11 # one thousand

    for i in range(1, 1000):
        total += calculateNumLength(i)
    
    duration = time.time() - start
    print(total, duration)
