# https://projecteuler.net/problem=3


def largest_prime_factor(num):
    i = 2

    while num != 1: 
        if num % i == 0: 
            num /= i
            i -= 1  
        i += 1

    return i
               

if __name__ == "__main__":
    ans = largest_prime_factor(600_851_475_143)
    print(ans)