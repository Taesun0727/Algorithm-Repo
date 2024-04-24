import sys
from collections import deque
sys.stdin = open('../../input.txt')
delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def bfs(num):
    queue = deque()
    queue.append((0, 0))
    visited = [[True] * N for _ in range(N)]
    visited[0][0] = False
    while queue:
        x, y = queue.popleft()
        if x == N-1 and y == N-1:
            return True
        for i in range(4):
            nx = x + delta[i][0]
            ny = y + delta[i][1]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] and abs(board[nx][ny]-board[x][y]) <= num:
                queue.append((nx, ny))
                visited[nx][ny] = False
    return False

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    start, end = 1, max(map(max,board)) - min(map(min,board))
    answer = 0
    while start <= end:
        mid = (start + end) // 2

        if bfs(mid):
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    print(answer)