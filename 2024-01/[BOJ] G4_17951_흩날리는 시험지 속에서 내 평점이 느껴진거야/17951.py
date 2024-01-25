import sys
sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    left, right = min(arr), sum(arr)

    while left <= right:
        mid = (left + right) // 2
        group = 0
        value = 0

        for i in range(N):
            if value + arr[i] < mid:
                value += arr[i]
            else:
                group += 1
                value = 0

        if group >= M:
            left = mid + 1
        else:
            right = mid - 1

    print(right)

