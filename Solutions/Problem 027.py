# https://projecteuler.net/problem=27

import math

def SieveOfEratothenes(n):
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False

    limit = int(math.sqrt(n))

    for i in range(limit):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j] = False

    return primes

def QuadraticPrimes(limit, primes):
    bestPair = (0, 0)
    bestSequence = 0


    for a in range(-limit, limit+1, 2):
        for b in range(-limit, limit+1, 2):
            if a + b < 0 or not primes[b]:
                continue
            
            n = 0
            while primes[n*n + a*n + b]:
                n += 1

            if n > bestSequence:
                bestSequence = n
                bestPair = (a, b)

    return bestPair

if __name__ == "__main__":
    upperLimit = 1997001
    primes = SieveOfEratothenes(upperLimit)
    result = QuadraticPrimes(999, primes)
    print(result[0] * result[1])
