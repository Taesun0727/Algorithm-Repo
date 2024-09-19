import sys

sys.stdin = open('../../input.txt')


def solution(num):
    global answer

    if num == 3:
        if bfs():
            answer = True
            return
    else:
        for x in range(N):
            for y in range(N):
                if board[x][y] == "X":
                    board[x][y] = "O"
                    solution(num + 1)
                    board[x][y] = "X"


def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for t in teacher:# 선생님의 위치에서
        for k in range(4): # 상/하/좌/우 탐색
            nx, ny = t

            while 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == "O":
                    break

                # 학생이 보이면 실패
                if board[nx][ny] == "S":
                    return False

                nx += dx[k]
                ny += dy[k]

    # 모두 통과하면 학생이 안보이는 것으로 성공
    return True

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    board = []
    teacher = []
    for i in range(N):
        board.append(list(map(str, sys.stdin.readline().split())))
        for j in range(N):
            if board[i][j] == "T":
                teacher.append((i, j))

    answer = False
    solution(0)
    if answer:
        print("YES")
    else:
        print("NO")
