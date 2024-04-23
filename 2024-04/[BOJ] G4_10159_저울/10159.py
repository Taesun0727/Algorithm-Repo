import sys
sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    board = [[0] * N for _ in range(N)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        board[a-1][b-1] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if board[i][k] and board[k][j]:
                    board[i][j] = 1

    for i in range(N):
        cnt = 0
        for j in range(N):
            if i == j:
                continue
            if not board[i][j] and not board[j][i]:
                cnt += 1
        print(cnt)