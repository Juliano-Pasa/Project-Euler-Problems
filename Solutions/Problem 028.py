# https://projecteuler.net/problem=28

def NumberSpiralDiagonals(n):
    total = 1 if n & 1 else 0

    for i in range(total+2, n+1, 2):
        total += 4*i*i - 6*i + 6

    return total

if __name__ == "__main__":
    result = NumberSpiralDiagonals(1001)
    print(result)