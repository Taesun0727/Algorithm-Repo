import sys

sys.setrecursionlimit(10 ** 6)

global_map = []
N = 0
M = 0
visited = []
count = 0
delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def in_range(x, y):
    if 0 > x or x >= N or 0 > y or y >= M:
        return False
    return True


def can_move(x, y):
    if "0" <= global_map[x][y] <= "9" and not visited[x][y]:
        return True
    return False


def find(x, y):
    global count
    visited[x][y] = True
    count += int(global_map[x][y])

    for i in range(4):
        nx = x + delta[i][0]
        ny = y + delta[i][1]
        if not in_range(nx, ny):
            continue

        if can_move(nx, ny):
            find(nx, ny)


def solution(maps):
    global global_map, N, M, visited, count
    global_map = maps
    N = len(maps)
    M = len(maps[0])
    visited = [[False] * M for _ in range(N)]
    answer = []

    for r in range(N):
        for c in range(M):
            if can_move(r, c):
                count = 0
                find(r, c)
                answer.append(count)

    answer.sort()

    if len(answer) == 0:
        answer = [-1]

    return answer