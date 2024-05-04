import sys
sys.stdin = open('../../input.txt')
sys.setrecursionlimit(10**6)

def dfs(cur, cur_value, max_value):
    global answer
    visited[cur] = False
    if cur == end:
        answer = cur_value - max_value
        return

    for next, cost in board[cur]:
        if visited[next]:
            dfs(next, cur_value+cost, max(max_value, cost))



if __name__ == "__main__":
    N, start, end = map(int, sys.stdin.readline().split())
    board = [[] for _ in range(N+1)]
    visited = [True] * (N+1)
    answer = 0
    for _ in range(N-1):
        s, e, c = map(int, sys.stdin.readline().split())
        board[s].append((e, c))
        board[e].append((s, c))

    dfs(start, 0, 0)

    print(answer)