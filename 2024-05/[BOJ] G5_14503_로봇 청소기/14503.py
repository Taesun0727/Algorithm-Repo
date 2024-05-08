import sys
sys.stdin = open('../../input.txt')

delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def clean():
    global answer;
    if board[van_x][van_y] == 0 and visited[van_x][van_y]:
        visited[van_x][van_y] = False
        answer += 1

def range_check(x, y):
    if 0 > x or x >= R or 0 > y or y >= C:
        return True
    return False

def clean_check():
    global van_x, van_y, van_d, van_status, answer
    ## 3번 청소되지 않은 빈칸 탐색후 있으면 변경후 return
    for i in range(4):
        van_d = (van_d + 3) % 4
        nx = van_x + delta[van_d][0]
        ny = van_y + delta[van_d][1]
        if range_check(nx, ny) or not visited[nx][ny]:
            continue
        if board[nx][ny] == 0:
            van_x, van_y = nx, ny
            return
    ## 있을경우 return으로 종료되고 아닐경우 2번 빈칸이 없는 경우 후진 실행
    nx = van_x + delta[(van_d+2)%4][0]
    ny = van_y + delta[(van_d+2)%4][1]
    if range_check(nx, ny) or board[nx][ny] == 1:
        van_status = False
        return
    else:
        van_x, van_y = nx, ny



if __name__ == "__main__":
    R, C = map(int, sys.stdin.readline().split())
    van_x, van_y, van_d = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
    visited = [[True] * C for _ in range(R)]
    answer = 0
    van_status = True

    while van_status:
        clean()
        clean_check()

    print(answer)