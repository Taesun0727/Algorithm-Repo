from collections import deque

global_maps = []
visited = []
N = 0
M = 0
start = (0, 0)
end = (0, 0)
lever = (0, 0)
delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def find_start_end():
    global start, end, lever
    for i in range(N):
        for j in range(M):
            if global_maps[i][j] == "S":
                start = (i, j)
            if global_maps[i][j] == "E":
                end = (i, j)
            if global_maps[i][j] == "L":
                lever = (i, j)


def move():
    global visited
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited[start[0]][start[1]][0] = 1
    while queue:
        x, y, status = queue.popleft()
        if x == end[0] and y == end[1] and status == 1:
            return
        for i in range(4):
            nx = x + delta[i][0]
            ny = y + delta[i][1]
            if 0 <= nx < N and 0 <= ny < M and global_maps[nx][ny] != "X" and not visited[nx][ny][status]:
                if nx == lever[0] and ny == lever[1] and status == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))
                else:
                    visited[nx][ny][status] = visited[x][y][status] + 1
                    queue.append((nx, ny, status))


def solution(maps):
    global global_maps, visited, N, M
    global_maps = maps
    N = len(maps)
    M = len(maps[0])
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    find_start_end()
    answer = -1
    move()
    if visited[end[0]][end[1]][1] > 0:
        answer = visited[end[0]][end[1]][1] - 1

    return answer