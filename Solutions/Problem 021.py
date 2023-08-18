# https://projecteuler.net/problem=21

import math

def FindDivisors(n):
    root = math.ceil(math.sqrt(n))
    divisors = [1]

    for i in range(2, root):
        if n % i != 0:
            continue

        divisors.append(i)
        divisors.append(n/i)

    if root == math.sqrt(n):
        divisors.append(root)

    return divisors


def FindAmicableNumber(n):
    divisorSum = sum(FindDivisors(n))

    if divisorSum <= n:
        return 0
    
    if n == sum(FindDivisors(divisorSum)):
        return divisorSum

    return 0


if __name__ == "__main__":
    amicableNumbersSum = 0

    for i in range(3, 100_000):
        pair = FindAmicableNumber(i)

        if pair:
            amicableNumbersSum += i
            amicableNumbersSum += pair

    print(amicableNumbersSum)