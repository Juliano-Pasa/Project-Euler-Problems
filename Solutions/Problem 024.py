# https://projecteuler.net/problem=24

import math

def IthPermutation(n):
    numbers = list(range(0, 10))
    result = ""
    n -= 1

    for i in range(9, -1, -1):
        fact = math.factorial(i)
        index = n // fact

        result += str(numbers[index])
        numbers.pop(index)
        
        n = n % fact

    return result


if __name__ == "__main__":
    result = IthPermutation(1_000_000)
    print(result)
    