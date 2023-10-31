import sys

sys.stdin = open('../../input.txt')

def finish_check():
    for i in range(N):
        now = i

        for j in range(H):
            if board[j][now]:
                now += 1
            elif now > 0 and board[j][now-1]:
                now -= 1
        if now != i:
            return False
    return True

def dfs(x, y, count):
    global result

    if finish_check():
        result = min(result, count)
        return

    if count == 3 or result <= count:
        return

    for i in range(x, H):
        if i == x:
            n_y = y
        else:
            n_y = 0

        for j in range(n_y, N-1):
            if not board[i][j] and not board[i][j+1]:
                if j > 0 and board[i][j-1]:
                    continue
                board[i][j] = True
                dfs(i, j+2, count+1)
                board[i][j] = False


if __name__ == "__main__":
    N, M, H = map(int, sys.stdin.readline().split())
    board = [[False] * N for _ in range(H)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        board[a-1][b-1] = True

    result = 4
    dfs(0, 0, 0)

    if result == 4:
        print(-1)
    else:
        print(result)