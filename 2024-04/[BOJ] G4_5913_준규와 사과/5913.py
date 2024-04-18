import sys
sys.stdin = open('../../input.txt')

delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def dfs(x, y, cnt):
    global answer
    if x == 4 and y == 4:
        if cnt == apple_count:
            answer += 1
        return

    for i in range(4):
        nx = x + delta[i][0]
        ny = y + delta[i][1]
        if 0 <= nx < 5 and 0 <= ny < 5 and board[nx][ny] == 1:
            board[nx][ny] = 0
            dfs(nx, ny, cnt+1)
            board[nx][ny] = 1

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    board = [[1]* 5 for _ in range(5)]
    apple_count = 25 - N
    answer = 0
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        board[x-1][y-1] -= 1

    board[0][0] = 0
    dfs(0, 0, 1)

    print(answer)