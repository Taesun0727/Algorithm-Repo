import sys

sys.stdin = open('../../input.txt')


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    board = list([0] * N for _ in range(N))
    answer = 0

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        board[a-1][b-1] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if board[i][k] == 1 and board[k][j] == 1:
                    board[i][j] = 1

    for i in range(N):
        known = 0
        for j in range(N):
            known += board[i][j] + board[j][i]

        if known == N-1:
            answer += 1

    print(answer)