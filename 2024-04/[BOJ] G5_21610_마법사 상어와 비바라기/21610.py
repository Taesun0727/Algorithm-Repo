import sys
sys.stdin = open('../../input.txt')

delta = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
delta2 = [[-1, -1], [-1, 1], [1, 1], [1, -1]]

def copy_water(x, y):
    count = 0
    for i in range(4):
        nx = x + delta2[i][0]
        ny = y + delta2[i][1]

        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > 0:
            count += 1
    return count

def move_cloud(x, y, d, s):
    nx = (x + delta[d][0] * s + N) % N
    ny = (y + delta[d][1] * s + N) % N
    return nx, ny

def make_cloud():
    global cloud
    tmp = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > 1 and (i, j) not in cloud:
                tmp.append([i, j])
                board[i][j] -= 2
    cloud = tmp

def find_answer():
    count = 0
    for i in range(N):
        for j in range(N):
            count += board[i][j]

    return count
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    cloud = [[N - 2, 0], [N - 2, 1], [N - 1, 0], [N - 1, 1]]
    for _ in range(M):
        d, s = map(int, sys.stdin.readline().split())

        for i in range(len(cloud)):
            cloud[i] = move_cloud(cloud[i][0], cloud[i][1], d-1, s)
        for x, y in cloud:
            board[x][y] += 1
        for x, y in cloud:
            board[x][y] += copy_water(x, y)

        make_cloud()
    print(find_answer())