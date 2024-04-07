import sys
sys.stdin = open('../../input.txt')

delta = [[0, -1], [1, 0], [0, 1], [-1, 0]]
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1), (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x,y,z in left]
down = [(-y, x, z) for x,y,z in left]
up = [(y, x, z) for x,y,z in left]
dic = {0: left, 1: down, 2: right, 3: up}

def move(x, y, d):
    global answer
    total = 0
    if y < 0:
        return
    for dx, dy, z in dic[d]:
        next_sand = 0
        nx = x + dx
        ny = y + dy
        if z == 0:
            next_sand = board[x][y] - total
        else:
            next_sand = int(board[x][y] * z)
            total += next_sand

        if 0 <= nx < N and 0 <= ny < N:
            board[nx][ny] += next_sand
        else:
            answer += next_sand

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    count = 0
    sx, sy = N // 2, N // 2
    answer = 0
    print(board)
    for i in range(2*N-1):
        d = i % 4
        if d == 0 or d == 2:
            count += 1
        for _ in range(count):
            nx = sx + delta[d][0]
            ny = sy + delta[d][1]
            move(nx, ny, d)
            sx, sy = nx, ny

    print(answer)