# https://projecteuler.net/problem=31

values = [200, 100, 50, 20, 10, 5, 2, 1]

def CoinSums(goal, current, startingIndex):
    if current > goal:
        return 0
    if current == goal:
        return 1

    total = 0

    for id, v in enumerate(values[startingIndex:]):
        total += CoinSums(goal, current + v, id + startingIndex)

    return total


if __name__ == "__main__":
    result = CoinSums(200, 0, 0)
    print(result)