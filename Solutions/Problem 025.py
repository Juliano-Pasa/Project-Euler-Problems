# https://projecteuler.net/problem=25

from logging.handlers import NTEventLogHandler
import math

calculatedFibos = {}

def nDigitFiboIndex(n):
    a = 1
    b = 1
    c = 2
    index = 2

    while (math.floor(math.log10(c)) + 1) < n:
        c = a + b
        a = b
        b = c
        index += 1
    return index

if __name__ == "__main__":
    print(nDigitFiboIndex(1000))