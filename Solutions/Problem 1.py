def sum_multiples(a, b, limit): # First solution
    ans = 0
    for i in range(limit): 
        ans += i * (i % a == 0 or i % b == 0)
    return ans

def sum_multiples_list(a, b, limit): # Solution found online
    return sum(i for i in range(limit) if (i % a == 0 or i % b == 0))

if __name__ == "__main__":
    ans = sum_multiples_list(3, 5, 1000)
    print(ans)