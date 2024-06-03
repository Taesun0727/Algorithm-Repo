import sys
sys.setrecursionlimit(10**8)

delta = [[1, 0], [0, -1], [0, 1], [-1, 0]]
d = ["d", "l", "r", "u"]
answer = "z"

def distance_cal(s_x, s_y, end_x, end_y):
    return abs(s_x - end_x) + abs(s_y - end_y)

def dfs(x, y, end_r, end_c, cur, count, n, m, k):
    global answer
    if k < count + distance_cal(x, y, end_r, end_c):
        return
    if count == k and x == end_r and y == end_c:
        answer = cur
        return
    for i in range(4):
        nx = x + delta[i][0]
        ny = y + delta[i][1]
        if 0 <= nx < n and 0 <= ny < m and cur < answer:
            dfs(nx, ny, end_r, end_c, cur+d[i], count+1, n, m, k)

def solution(n, m, x, y, r, c, k):
    if distance_cal(x, y, r, c) > k or (distance_cal(x, y, r, c) - k) % 2:
        return "impossible"
    dfs(x-1, y-1, r-1, c-1, "", 0, n, m, k)

    return answer