# https://projecteuler.net/problem=4

def transform_to_palindrome(num): 
    """ Creates a palindrome by reversing a given number

        Parameters:
        num (int): Number that will be reversed to create a palindrome (eg. 123 -> 123,321)

        Returns:
        int: A palindrome number with an even number of digits
    """

    new_number = num
    aux_number = 0
    power = 0

    while num > 0: # While loop to reverse a given number
        aux_number *= 10
        aux_number += num % 10    
        num = num // 10
        power += 1

    new_number *= 10**power # Multiply the original number by its size to "fit" the reversed number at the end
    new_number += aux_number # Add the reversed number at the end of the new palindrome number

    return new_number


def find_3digit_factors(num):
    for i in range(999, 100, -1): # We only need to test 3-digit divisors
        if num % i == 0 and 1000 > num/i > 100:
            return True    

    return False


def find_largest_palindrome(limit):
    """ Finds the largest palindrome that is a product of 2 3-digit numbers

        Parameters:
        limit (int): First half of the largest palindrome that COULD be the product of 2 3-digit numbers

        Returns:
        int: Largest palindrome found
    """

    while limit != 0:
        palindrome = transform_to_palindrome(limit)
        if find_3digit_factors(palindrome):
            return palindrome
        limit -= 1

    return limit


if __name__ == "__main__":
    ans = find_largest_palindrome(997)
    print(ans)