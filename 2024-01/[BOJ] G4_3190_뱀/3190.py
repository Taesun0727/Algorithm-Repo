import sys
from collections import deque
sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    A_C = int(sys.stdin.readline())
    board = [[0] * N for _ in range(N)]
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dic = {'L': -1, 'D': 1}
    board[0][0] = 1
    snake = deque()

    for _ in range(A_C):
        x, y = map(int, sys.stdin.readline().split())
        board[x-1][y-1] = 2

    M_C = int(sys.stdin.readline())
    queue = deque()

    for _ in range(M_C):
        value, D = sys.stdin.readline().split()
        queue.append((int(value)+1, D))

    answer = 0
    head = (0, 0)
    current_d = 0
    snake.append((0, 0))

    while True:
        answer += 1
        if queue and answer == queue[0][0]:
            current_d = (dic[queue[0][1]] + current_d) % 4
            queue.popleft()

        nx, ny = head[0]+delta[current_d][0], head[1]+delta[current_d][1]

        if 0 > nx or N <= nx or 0 > ny or N <= ny:
            break

        if board[nx][ny] == 2:
            board[nx][ny] = 1
            snake.append((nx, ny))
        elif board[nx][ny] == 0:
            board[nx][ny] = 1
            snake.append((nx, ny))
            tx, ty = snake.popleft()
            board[tx][ty] = 0
        else:
            break
        head = (nx, ny)

    print(answer)
