# https://projecteuler.net/problem=30

powers = {'0':0, '1':1, '2':32, '3':243, '4':1024, '5':3125, '6':7776, '7':16807, '8':32768, '9':59049}

def SumDigitPowers(n):
    total = 0
    for d in str(n):
        total += powers[d]

    return total

def DigitFifthPowers():
    numbersSum = 0

    for i in range(10, 300_000):
        if i == SumDigitPowers(i):
            numbersSum += i

    return numbersSum

if __name__ == "__main__":
    result = DigitFifthPowers()
    print(result)