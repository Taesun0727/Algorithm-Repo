import sys
sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    N, M, H = map(int, sys.stdin.readline().split())
    dp = [[1] + [0] * (H) for _ in range(N+1)]

    for i in range(1, N+1):
        dp[i] = dp[i-1].copy()
        blocks = list(map(int, sys.stdin.readline().split()))
        for block in blocks:
            for h in range(block, H+1):
                dp[i][h] += dp[i-1][h-block]

    print(dp[N][H] % 10007)