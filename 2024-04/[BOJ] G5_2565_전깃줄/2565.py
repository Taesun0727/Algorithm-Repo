import sys

sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    line = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dp = [1] * N
    line.sort()

    for i in range(1, N):
        for j in range(0, i):
            if line[j][1] < line[i][1]:
                dp[i] = max(dp[i], dp[j]+1)

    print(N-max(dp))