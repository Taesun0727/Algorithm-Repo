import sys
from collections import deque
sys.stdin = open('../../input.txt')

def bfs():
    global result
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1

    while queue:
        x, y, status = queue.popleft()
        if x == N-1 and y == M-1:
            return
        for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nx = x + dx
            ny = y + dy
            if 0 > nx or nx >= N or 0 > ny or ny >= M:
                continue
            if board[nx][ny] == 1 and status == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
            elif board[nx][ny] == 0 and visited[nx][ny][status] == -1:
                visited[nx][ny][status] = visited[x][y][status] + 1
                queue.append((nx, ny, status))

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
    visited = [[[-1] * 2 for _ in range(M)] for _ in range(N)]
    result = 0
    bfs()
    print(max(visited[N-1][M-1]))