# https://projecteuler.net/problem=39

calculated = set([])
rank = {}

def OptimalP(limit):
    for n in range(1, 16):
        for m in range(n+1, 22):
            a = m^2 - n^2
            b = 2*m*n
            c = m^2 + n^2

            total = a + b + c
            if total > 1000 or (a, b, c) in calculated:
                break

            kTotal = total
            k = 1
            while kTotal <= 1000:
                calculated.add((a*k, b*k, c*k))

                if kTotal not in rank:
                    rank[kTotal] = 1
                else:
                    rank[kTotal] += 1

                k += 1
                kTotal = total * k

    max_key = next(iter(rank))

    for k in rank:
        if rank[k] > rank[max_key]:
            max_key = k

    return max_key

if __name__ == "__main__":
    result = OptimalP(1000)
    print(result)