def fibonacci_even_sum(limit):
    prev_term = 0
    new_term = 1
    aux = new_term
    ans = 0

    while (new_term < limit):
        ans += new_term * (not (new_term % 2))

        aux = new_term
        new_term = new_term + prev_term
        prev_term = aux

    return ans

if __name__ == "__main__":
    ans = fibonacci_even_sum(4_000_000)
    print(ans)