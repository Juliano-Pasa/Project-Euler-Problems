# https://projecteuler.net/problem=5


def find_highest_power(num, limit):
    """ Finds the highest power of a number below a limit

        Parameters:
        limit (int): Limit that number powers cant go above

        Returns: 
        int: Highest power of a number below the limit
    """
    power = 0
    while num**power < limit:
        power += 1

    return power - 1


def decompose_sequence_factors(limit):
    """ Decomposes the prime factors of a sequence from 1 to limit
        The exponent of a given factor is the highest exponent among all numbers in the sequence that have that factor

        Parameters: 
        limit (int): Last number of the sequence not included 

        Returns:
        int: Product of all factors found    
    """

    factors = [False] * (limit - 2)
    product = 1

    for i in range(2, limit):
        product *= i
    
    i = 2
    while product != 1: 
        if product % i == 0:
            factors[i-2] = True
            product = product // i
            i -= 1
        i += 1

    ans = 1
    for i, val in enumerate(factors):
        if val:
            ans *= (i+2)**find_highest_power(i+2, limit)

    return ans

if __name__ == "__main__":
    ans = decompose_sequence_factors(31)
    print(ans)
