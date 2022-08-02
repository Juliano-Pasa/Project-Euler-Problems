# https://projecteuler.net/problem=1

def sum_multiples(a, b, limit):
    ans = 0
    for i in range(limit): 
        ans += i * (i % a == 0 or i % b == 0)
    return ans

if __name__ == "__main__":
    ans = sum_multiples(3, 5, 1000)
    print(ans)