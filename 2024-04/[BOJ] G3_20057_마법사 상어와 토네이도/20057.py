import sys
from collections import deque
sys.stdin = open('../../input.txt')

delta = [[-1, 0], [1, 0], [0, 1], [0, -1]]

def find_ice(x, y):
    global second_answer, check
    check[x][y] = False
    queue = deque()
    queue.append((x, y))
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + delta[i][0]
            ny = y + delta[i][1]

            if 0 <= nx < len_board and 0 <= ny < len_board and board[nx][ny] > 0 and check[nx][ny]:
                check[nx][ny] = False
                cnt += 1
                queue.append((nx, ny))

    second_answer = max(second_answer, cnt)

def find_answer():
    global first_answer
    for i in range(len_board):
        for j in range(len_board):
            first_answer += board[i][j]
            if board[i][j] > 0 and check[i][j]:
                find_ice(i, j)


def melting_ice():
    melting = []
    for i in range(len_board):
        for j in range(len_board):
            if board[i][j] > 0:
                count = 0
                for k in range(4):
                    nx = i + delta[k][0]
                    ny = j + delta[k][1]

                    if 0 <= nx < len_board and 0 <= ny < len_board and board[nx][ny] > 0:
                        count += 1
                if count < 3:
                    melting.append((i, j))
    for x, y in melting:
        board[x][y] -= 1

def rotate(x, y, num):
    temp = [row[y:y+num] for row in board[x:x+num]]
    for r in range(num):
        for c in range(num):
            board[x+c][y+num-1-r] = temp[r][c]


def fireStorm(num):
    for i in range(0, len_board, 2**num):
        for j in range(0, len_board, 2**num):
            rotate(i, j, 2**num)

if __name__ == "__main__":
    N, Q = map(int, sys.stdin.readline().split())
    len_board = 2**N
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(len_board)]
    L = list(map(int, sys.stdin.readline().split()))
    check = [[True] * len_board for _ in range(len_board)]
    first_answer, second_answer = 0, 0

    for x in L:
        fireStorm(x)
        melting_ice()
    find_answer()

    print(first_answer)
    print(second_answer)
