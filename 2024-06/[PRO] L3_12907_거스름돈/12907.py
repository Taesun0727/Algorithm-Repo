def solution(n, money):
    dp = [1] + [0] * n

    for m in money:
        for nxt in range(m, n + 1):
            dp[nxt] += dp[nxt - m]

    return dp[n] % 1000000007