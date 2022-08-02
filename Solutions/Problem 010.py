# https://projecteuler.net/problem=10

def find_primes_sum(limit): 
    primes = [True] * limit # Sieve of eratosthenes
    primes[0] = primes[1] = False
    total = 0

    for p, val in enumerate(primes):
        if val: # All primes will be True
            primes[p*2::p] = [False] * len(primes[p*2::p]) # All prime multiples become False
            total += p # Sums all primes
    
    return total

if __name__ == "__main__":
    ans = find_primes_sum(2_000_000)
    print(ans)