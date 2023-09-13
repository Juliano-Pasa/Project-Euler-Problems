# https://projecteuler.net/problem=23

import math

def DivisorsSum(n):
    root = math.ceil(math.sqrt(n))
    divisorsSum = 1

    for i in range(2, root):
        if n % i != 0:
            continue

        divisorsSum += i
        divisorsSum += n/i

    if root == math.sqrt(n):
        divisorsSum += root

    return divisorsSum

def NonAbundantSum():
    totalSum = 0
    abundant = set([a for a in range(12, 28112) if a < DivisorsSum(a)])

    for n in range(1, 28124):
        for e in abundant:
            if (n - e) in abundant:
                break
            if n <= e:
                totalSum += n
                break

    return totalSum

if __name__ == "__main__":
    result = NonAbundantSum()
    print(result)