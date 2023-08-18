# https://projecteuler.net/problem=40

def GetNumberByIndex(n):
    i = 1
    current = 1
    currentSize = 1
    previous = i

    while i <= n:
        previous = i
        i += current*9*currentSize
        current *= 10
        currentSize += 1

    value = current/10 + (n - previous)//(currentSize - 1)
    remainder = (n - previous) % (currentSize - 1)

    return int(str(value)[remainder])

if __name__ == "__main__":
    total = 1
    i = 1

    while i < 1_000_001:
        total *= GetNumberByIndex(i)
        i *= 10

    print(total)