import sys
sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    dp = [[0] * N for _ in range(N)]

    for len_arr in range(N):
        for start in range(N-len_arr):
            end = start + len_arr
            if start == end:
                dp[start][end] = 1
            elif arr[start] == arr[end]:
                if start+1 == end:
                    dp[start][end] = 1
                elif dp[start+1][end-1]:
                    dp[start][end] = 1

    T = int(sys.stdin.readline())

    for _ in range(T):
        start, end = map(int, sys.stdin.readline().split())
        print(dp[start-1][end-1])
