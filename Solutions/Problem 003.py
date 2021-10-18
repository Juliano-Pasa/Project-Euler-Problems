
def largest_prime_factor(num):
    i = 2

    # If num == 1 it means it was last divided by its remaining factor
    # Since i starts at 2 and goes up, the last remaining factor is the largest one

    while num != 1: 
        if num % i == 0: 
            num /= i # Divides the number by one of its prime factor
            i -= 1 # Adjusts i value to repeat prime factor      
        i += 1

    return i # Return i (largest prime factor) as soon as loop ends
               

if __name__ == "__main__":
    ans = largest_prime_factor(600_851_475_143)
    print(ans)