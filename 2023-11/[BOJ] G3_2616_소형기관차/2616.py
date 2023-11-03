import sys

sys.stdin = open('../../input.txt')


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    train = [0] + list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    dp = [[0] * (N+1) for _ in range(4)]

    for i in range(1, 4):
        for j in range(i*M, N+1):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-M] + sum(train[j-M+1:j+1]))

    print(dp[3][N])