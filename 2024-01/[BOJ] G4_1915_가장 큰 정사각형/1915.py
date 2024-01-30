import sys
sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
    answer = 0

    for i in range(N):
        for j in range(M):
            if i > 0 and j > 0 and board[i][j] == 1:
                board[i][j] += min(board[i][j-1], board[i-1][j], board[i-1][j-1])
            answer = max(answer, board[i][j])

    print(answer*answer)