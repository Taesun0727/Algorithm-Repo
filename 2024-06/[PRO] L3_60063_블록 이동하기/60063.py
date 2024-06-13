from collections import deque
delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
global_board = []
N = 0
M = 0

def can_move_check(x, y):
    if x < 0 or x >= N or y < 0 or y >= N or global_board[x][y] == 1:
        return False
    return True

def move(cur1, cur2):
    tmp = []
    for i in range(4):
        n_cur1 = ((cur1[0] + delta[i][0], cur1[1] + delta[i][1]))
        n_cur2 = ((cur2[0] + delta[i][0], cur2[1] + delta[i][1]))
        if can_move_check(n_cur1[0], n_cur1[1]) and can_move_check(n_cur2[0], n_cur2[1]):
            tmp.append((n_cur1, n_cur2))
    if cur1[0] == cur2[0]:
        for d in [-1, 1]:
            if can_move_check(cur1[0]+d, cur1[1]) and can_move_check(cur2[0]+d, cur2[1]):
                tmp.append((cur1, (cur1[0]+d, cur1[1])))
                tmp.append((cur2, (cur2[0]+d, cur2[1])))
    else:
        for d in [-1, 1]:
            if can_move_check(cur1[0], cur1[1]+d) and can_move_check(cur2[0], cur2[1]+d):
                tmp.append(((cur1[0], cur1[1]+d), cur1))
                tmp.append(((cur2[0], cur2[1]+d), cur2))
    return tmp

def solution(board):
    global global_board, N, M
    global_board = board
    N = len(board)
    M = len(board[0])
    queue = deque([((0, 0), (0, 1), 0)])
    visited = set()
    visited.add(((0, 0), (0, 1)))
    while queue:
        cur1, cur2, count = queue.popleft()
        if cur1 == (N-1, N-1) or cur2 == (N-1, N-1):
            return count
        for nxt in move(cur1, cur2):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((*nxt, count+1))