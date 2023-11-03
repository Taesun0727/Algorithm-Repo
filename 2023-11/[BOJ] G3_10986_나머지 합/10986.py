import sys

sys.stdin = open('../../input.txt')


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    count = [0] * M
    prefix_sum = 0

    for i in range(N):
        prefix_sum += arr[i]
        count[prefix_sum % M] += 1

    result = count[0]

    for i in range(M):
        result += count[i] * (count[i]-1) // 2

    print(result)

# https://code-angie.tistory.com/26