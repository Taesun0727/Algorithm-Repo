from collections import deque

def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])
    visited = [[0] * M for _ in range(N)]
    delta = [[1, 0], [0, -1], [-1, 0], [0, 1]]

    def find_start_finish():
        start = (0, 0)
        finish = (0, 0)
        for i in range(N):
            for j in range(M):
                if board[i][j] == "R":
                    start = (i, j)
                if board[i][j] == "G":
                    finish = (i, j)
        return start, finish

    def bfs():
        queue = deque()
        queue.append((start[0], start[1]))
        visited[start[0]][start[1]] = 1
        while queue:
            x, y = queue.popleft()
            if x == finish[0] and y == finish[1]:
                return visited[x][y]
            for i in range(4):
                nx, ny = x, y
                while True:
                    nx += delta[i][0]
                    ny += delta[i][1]
                    if 0 > nx or N <= nx or 0 > ny or M <= ny or board[nx][ny] == "D":
                        nx -= delta[i][0]
                        ny -= delta[i][1]
                        break
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
        return -1

    start, finish = find_start_finish()
    answer = bfs()

    if answer > 0:
        answer -= 1

    return answer