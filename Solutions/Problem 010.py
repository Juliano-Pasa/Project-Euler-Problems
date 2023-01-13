# https://projecteuler.net/problem=10


def find_primes_sum(limit): 
    primes = [True] * limit
    primes[0] = primes[1] = False
    total = 0

    for p, val in enumerate(primes):
        if val:
            primes[p*2::p] = [False] * len(primes[p*2::p])
            total += p
    
    return total

if __name__ == "__main__":
    ans = find_primes_sum(2_000_000)
    print(ans)