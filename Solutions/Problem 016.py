# https://projecteuler.net/problem=16


import time

def calculateLargePowerOfTwo(power):
    result = [1]
    
    while power != 0:
        carry = 0
        for i in range(len(result)):
            term = result[i]
            result[i] = (term*2 + carry) % 10
            carry = 1 if term > 4 else 0
        if carry:
            result.append(carry)
        power -= 1
    
    return result[::-1]

if __name__ == "__main__":
    start = time.time()
    num = calculateLargePowerOfTwo(1000)
    sumOfDigits = sum(num)
    duration = time.time() - start
    print(sumOfDigits, duration)
