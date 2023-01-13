# https://projecteuler.net/problem=7


from math import ceil, log

def nth_prime_upper_bound(n):
    if n < 6:
        return 100
    return ceil(n * (log(n) + log(log(n))))


def find_nth_prime(index):
    limit = nth_prime_upper_bound(index)

    primes = [True] * limit
    primes[0] = primes[1] = False
    total = 0

    for p, val in enumerate(primes):
        if val:
            primes[p*2::p] = [False] * len(primes[p*2::p])
            total += 1

        if total == index:
            return p


if __name__ == "__main__":
    ans = find_nth_prime(10_001)
    print(ans)