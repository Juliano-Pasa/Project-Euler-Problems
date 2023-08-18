# https://projecteuler.net/problem=20

import math

if __name__ == "__main__":
    num = math.factorial(100)
    result = sum(list(map(int, str(num))))

    print(result)