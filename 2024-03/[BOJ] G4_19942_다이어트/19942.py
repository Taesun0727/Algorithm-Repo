import sys
sys.stdin = open('../../input.txt')

def dfs(idx, current_nut, current_cost, select_food):
    global cost, result
    if idx == N:
        if current_nut[0] >= nut[0] and current_nut[1] >= nut[1] and current_nut[2] >= nut[2] and current_nut[3] >= nut[3]:
            if cost > current_cost:
                cost = current_cost
                result = list(select_food)
        return
    if current_cost > cost:
        return

    for i in range(idx, N):
        current_nut[0] += board[idx][0]
        current_nut[1] += board[idx][1]
        current_nut[2] += board[idx][2]
        current_nut[3] += board[idx][3]
        select_food.append(idx+1)
        dfs(idx+1, current_nut, current_cost+board[idx][4], select_food)
        current_nut[0] -= board[idx][0]
        current_nut[1] -= board[idx][1]
        current_nut[2] -= board[idx][2]
        current_nut[3] -= board[idx][3]
        select_food.pop()
        dfs(idx+1, current_nut, current_cost, select_food)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    nut = list(map(int, sys.stdin.readline().split()))
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    cost = sys.maxsize
    result = []

    dfs(0, [0, 0, 0, 0], 0, [])

    print(cost)
    print(*result)