def countDivisors(num):
    totalDivisors = 1
    count = 1
    i = 2    

    while num != 1:
        if num % i == 0:
            count += 1
            num = num/i
        else:
            i += 1
            totalDivisors *= count
            count = 1
    
    totalDivisors *= count
    return totalDivisors

if __name__ == "__main__":
    divisors = 0
    i = 0
    num = 0

    while divisors <= 500:
        i += 1
        num += i
        divisors = countDivisors(num)
    
    print(num)
