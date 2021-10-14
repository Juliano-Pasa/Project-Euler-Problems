def sum_multiples(a, b, lim): # First solution
    sum = 0
    for i in range(lim): 
        sum += i * (i % a == 0 or i % b == 0)
    return sum

def sum_multiples_list(a, b, lim): # Solution found online
    return sum(i for i in range(lim) if (i % a == 0 or i % b == 0))

if __name__ == "__main__":
    total = sum_multiples_list(3, 5, 1000)
    print(total)