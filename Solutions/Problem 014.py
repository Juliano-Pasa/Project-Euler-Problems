# https://projecteuler.net/problem=14


import time

def collatzSequenceLength(num):
    count = 1

    while num != 1:
        num = 3*num + 1 if num & 1 else num // 2
        count += 1

    return count


def findLongestSequence(limit):
    longest = 0
    bestNum = 0

    for i in range(1, limit):
        actualSequence = 0
        if i % 3 == 0:
            if i & 1:
                actualSequence = collatzSequenceLength(i)
            else:
                actualSequence = longest + 1 if i // 2 == bestNum else longest
        
        elif i % 3 == 1:
            if i & 1:
                actualSequence = collatzSequenceLength(i)

        else:
            if not i & 1:
                actualSequence = longest + 1 if i // 2 == bestNum else longest                

        if actualSequence > longest:
            longest = actualSequence
            bestNum = i

    return bestNum, longest

if __name__ == "__main__":
    start = time.time()
    result, sequence = findLongestSequence(1_000_000)
    duration = time.time() - start
    print(result, sequence, duration)