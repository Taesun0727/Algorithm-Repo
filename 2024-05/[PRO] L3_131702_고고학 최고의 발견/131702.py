from itertools import product
import sys

global_clockHands = []
N = 0
delta = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]


def in_range(x, y):
    if 0 > x or x >= N or 0 > y or y >= N:
        return True
    return False


def rotate_clockHands(x, y, t, board):
    for i in range(5):
        nx = x + delta[i][0]
        ny = y + delta[i][1]
        if in_range(nx, ny):
            continue
        board[nx][ny] = (board[nx][ny] + t) % 4


def solution(clockHands):
    global global_clockHands, N
    global_clockHands = clockHands
    N = len(global_clockHands)
    answer = sys.maxsize
    for case in product(range(4), repeat=N):
        board = [row[:] for row in global_clockHands]

        for i in range(N):
            rotate_clockHands(0, i, case[i], board)
        count = sum(case)

        for i in range(1, N):
            for j in range(N):
                if board[i - 1][j]:
                    tmp = 4 - board[i - 1][j]
                    rotate_clockHands(i, j, tmp, board)
                    count += tmp

        if sum(board[N - 1]):
            continue

        answer = min(answer, count)

    return answer