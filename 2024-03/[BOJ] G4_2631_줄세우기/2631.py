import sys
sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    arr = [0]
    dp = [1] * (N+1)
    for i in range(N):
        arr.append(int(sys.stdin.readline()))

    for i in range(1, N+1):
        for j in range(1, i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(N-max(dp))