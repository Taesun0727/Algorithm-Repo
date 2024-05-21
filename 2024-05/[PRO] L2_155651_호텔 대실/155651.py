global_board = []
N = 0

def finish_check(status):
    for row in global_board:
        if row == [status, status, status]:
            return True

    for col in range(N):
        if [global_board[row][col] for row in range(N)] == [status, status, status]:
            return True

    if [global_board[0][0], global_board[1][1], global_board[2][2]] == [status, status, status]:
        return True
    if [global_board[2][0], global_board[1][1], global_board[0][2]] == [status, status, status]:
        return True

    return False


def count_check():
    o_count, x_count = 0, 0
    for i in range(N):
        for j in range(N):
            if global_board[i][j] == "O":
                o_count += 1
            elif global_board[i][j] == "X":
                x_count += 1

    return o_count, x_count


def solution(board):
    global global_board, N
    global_board = [list(row) for row in board]
    N = len(global_board)

    o_count, x_count = count_check()

    if not (o_count == x_count or o_count == x_count + 1):
        return 0

    if finish_check("O") and finish_check("X"):
        return 0

    if finish_check("O") and o_count != x_count + 1:
        return 0

    if finish_check("X") and o_count != x_count:
        return 0

    return 1