def FindRecurringCycleLen(n):
    remainders = {}
    index = 0
    remainder = 1

    while remainder not in remainders:
        if remainder < n:
            remainders[remainder] = index
            index += 1
            remainder *= 10
        else:
            remainder %= n

    if 0 in remainders:
        return 0

    return len(remainders) - remainders[remainder]


if __name__ == "__main__":
    result = 0
    for i in range(3, 1000):
        size = FindRecurringCycleLen(i)
        result = i if size > result else result

    print(result)
    