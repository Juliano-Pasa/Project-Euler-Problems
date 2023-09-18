# https://projecteuler.net/problem=29

def DistinctPowers(limit):
    powers = set([])

    for a in range(2, limit+1):
        for b in range(2, limit+1):
            powers.add(a**b)

    return len(powers)

if __name__ == "__main__":
    result = DistinctPowers(100)
    print(result)