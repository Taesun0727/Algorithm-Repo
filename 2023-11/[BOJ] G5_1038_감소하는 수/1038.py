import sys
from itertools import combinations

sys.stdin = open('../../input.txt')


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    result = []

    for i in range(1, 11):
        for x in combinations(range(10), i):
            tmp = "".join(list(map(str, reversed(list(x)))))
            result.append(int(tmp))

    result.sort()

    if N >= len(result):
        print(-1)
    else:
        print(result[N])