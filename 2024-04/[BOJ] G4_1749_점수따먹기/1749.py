import sys
sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    board = [[0] * (M+1)] + [([0] + list(map(int, sys.stdin.readline().split()))) for _ in range(N)]
    answer = -10000

    for i in range(1, N+1):
        r_prefix = [0] * (M+1)
        for j in range(i, N+1):
            c_prefix = [0] * (M+1)
            for k in range(1, M+1):
                r_prefix[k] += board[j][k]
                c_prefix[k] = max(r_prefix[k], c_prefix[k-1] + r_prefix[k])
                answer = max(c_prefix[k], answer)

    print(answer)