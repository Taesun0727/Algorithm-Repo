import sys
sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    H, W = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    answer = 0

    for i in range(1, W-1):
        left_max = max(arr[:i])
        right_max = max(arr[i+1:])

        water = min(left_max, right_max)

        if arr[i] < water:
            answer += water - arr[i]

    print(answer)