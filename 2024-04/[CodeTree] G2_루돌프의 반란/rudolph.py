import sys
sys.stdin = open('../../input.txt')

rudolph_delta = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
santa_delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def plus_score():
    for i in range(P):
        if santas_sataus[i]:
            santa_score[i] += 1

def next_santa(x, y, d, status):
    for i in range(P):
        santa_x, santa_y = santas[i]
        if santa_x == x and santa_y == y:
            if status == 0:
                nx = x + rudolph_delta[d][0]
                ny = y + rudolph_delta[d][1]
            else:
                nx = x + santa_delta[(d+2)%4][0]
                ny = y + santa_delta[(d+2)%4][1]
            next_santa(nx, ny, d, status)
            alive_check(nx, ny, i)
            santas[i] = (nx, ny)

def alive_check(x, y, idx):
    if 0 > x or N <= x or 0 > y or N <= y:
        santas_sataus[idx] = False

def santas_move(time):
    for i in range(P):
        if santas_faint[i] >= time or not santas_sataus[i]:
            continue
        santa_x, santa_y = santas[i]
        distance = (rudolph_x - santa_x) ** 2 + (rudolph_y - santa_y) ** 2
        find_x, find_y, d = -1, -1, -1
        for j in range(4):
            nx = santa_x + santa_delta[j][0]
            ny = santa_y + santa_delta[j][1]
            tmp = (rudolph_x - nx) ** 2 + (rudolph_y - ny) ** 2
            if distance > tmp and (nx, ny) not in santas:
                find_x, find_y, d = nx, ny, j
                distance = tmp
        if find_x != -1 and find_y != -1:
            santas[i] = (find_x, find_y)
            if find_x == rudolph_x and find_y == rudolph_y:
                santa_score[i] += D
                nx = find_x + santa_delta[(d+2)%4][0] * D
                ny = find_y + santa_delta[(d+2)%4][1] * D
                next_santa(nx, ny, d, 1)
                alive_check(nx, ny, i)
                santas[i] = (nx, ny)
                santas_faint[i] = time + 1

def rudolph_move(x, y, time):
    global rudolph_x, rudolph_y
    if x == -1 and y == -1:
        return
    distance = (x - rudolph_x) ** 2 + (y - rudolph_y) ** 2
    find_x, find_y = -1, -1
    d = -1
    for i in range(8):
        nx = rudolph_x + rudolph_delta[i][0]
        ny = rudolph_y + rudolph_delta[i][1]
        tmp = (x - nx) ** 2 + (y - ny) ** 2
        if tmp < distance:
            find_x, find_y = nx, ny
            distance = tmp
            d = i

    rudolph_x, rudolph_y = find_x, find_y

    for i in range(P):
        santa_x, santa_y = santas[i]
        if find_x == santa_x and find_y == santa_y:
            santa_score[i] += C
            nx = santa_x + rudolph_delta[d][0] * C
            ny = santa_y + rudolph_delta[d][1] * C
            next_santa(nx, ny, d, 0)
            alive_check(nx, ny, i)
            santas[i] = (nx, ny)
            santas_faint[i] = time+1


def find_near_santa():
    find_x, find_y, distance = -1, -1, sys.maxsize
    for i in range(P):
        if not santas_sataus[i]:
            continue
        santa_x, santa_y = santas[i]
        tmp = abs(rudolph_x-santa_x) ** 2 + abs(rudolph_y-santa_y) ** 2
        if tmp < distance:
            find_x, find_y = santa_x, santa_y
            distance = tmp
        if tmp == distance:
            if santa_x > find_x:
                find_x, find_y = santa_x, santa_y
            if santa_x == find_x:
                if santa_y > find_y:
                    find_x, find_y = santa_x, santa_y

    return find_x, find_y

if __name__ == "__main__":
    N, M, P, C, D = map(int, sys.stdin.readline().split())

    rudolph_x, rudolph_y = map(int, sys.stdin.readline().split())
    rudolph_x, rudolph_y = rudolph_x-1, rudolph_y-1
    santas = [(0, 0) for _ in range(P)]
    santas_sataus = [True] * P
    santa_score = [0] * P
    santas_faint = [-1] * P
    for _ in range(P):
        santa_num, santa_x, santa_y = map(int, sys.stdin.readline().split())
        santas[santa_num-1] = (santa_x-1, santa_y-1)
    for time in range(M):
        find_x, find_y = find_near_santa()
        rudolph_move(find_x, find_y, time)
        santas_move(time)
        plus_score()
    print(*santa_score)