def find_sum_triplet(total):
    ''' Function to find pythagorean triples using their sum

        Parameters:
        total (int): Sum of the pythagorean triples

        Returns:
        a, b and c (int): The triplets
    '''

    aux = 0
    m = 2
    while m <= (total/2)**0.5: # Biggest value of m so that the sum is lower than total  
        for n in range(m):
            aux = 2*m*(n + m)
            if aux == total:
                return 2*m*n, m**2 + n**2, m**2 - n**2
        m += 1

    return 0, 0, 0

if __name__ == "__main__":
    a, b, c = find_sum_triplet(1000)
    ans = a * b * c
    print(ans)
