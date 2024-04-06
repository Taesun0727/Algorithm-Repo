import sys
sys.stdin = open('../../input.txt')

delta = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

def comb_fireball(x, y, cnt_fireballs):
    total_m, total_s, even_check = 0, 0, 0
    for m, s, d in board[x][y]:
        total_m += m
        total_s += s
        if d % 2 == 0:
            even_check += 1

    total_m = total_m // 5
    if total_m == 0:
        return
    total_s = total_s // cnt_fireballs
    if even_check == 0 or even_check == cnt_fireballs:
        check = True
    else:
        check = False

    for i in range(8):
        if check:
            if i % 2 != 0:
                continue
        else:
            if i % 2 == 0:
                continue
        fireballs.append((x, y, total_m, total_s, i))


def find_fireball():
    for i in range(N):
        for j in range(N):
            len_board = len(board[i][j])
            if len_board == 1:
                m, s, d = board[i][j][0]
                fireballs.append((i, j, m, s, d))
            if len_board > 1:
                comb_fireball(i, j, len_board)


def go_fireball():
    for r, c, m, s, d in fireballs:
        nx = (r + delta[d][0] * s + N) % N
        ny = (c + delta[d][1] * s + N) % N
        board[nx][ny].append((m, s, d))

def find_answer():
    answer = 0
    for r, c, m, s, d in fireballs:
        answer += m
    return answer

if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().split())
    board = [list(list() for _ in range(N)) for _ in range(N)]
    fireballs = []
    for _ in range(M):
        r, c, m, s, d = map(int, sys.stdin.readline().split())
        fireballs.append((r-1, c-1, m, s, d))
    for _ in range(K):
        go_fireball()
        fireballs = []
        find_fireball()
        board = [list(list() for _ in range(N)) for _ in range(N)]

    print(find_answer())