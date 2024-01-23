import sys
from collections import deque
sys.stdin = open('../../input.txt')

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        qx, qy = q.popleft()

        for dx, dy in ([(-1, 0), (0, 1), (1, 0), (0, -1)]):
            nx = qx + dx
            ny = qy + dy

            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0:
                    visited[qx][qy] += 1

                if not visited[nx][ny] and board[nx][ny] != 0:
                    q.append((nx, ny))
                    visited[nx][ny] = True

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    time = 0

    while True:
        count = 0
        visited = [[0] * M for _ in range(N)]

        for i in range(N):
            for j in range(M):
                if not visited[i][j] and board[i][j] > 0:
                    bfs(i, j)
                    count += 1

        for i in range(N):
            for j in range(M):
                if visited[i][j]:
                    board[i][j] -= (visited[i][j] - 1)
                    if board[i][j] < 0:
                        board[i][j] = 0

        time += 1
        if count == 0:
            print(0)
            exit()
        if count >= 2:
            break

    print(time-1)