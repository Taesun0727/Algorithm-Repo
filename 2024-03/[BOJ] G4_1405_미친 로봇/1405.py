import sys
sys.stdin = open('../../input.txt')

delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def dfs(x, y, visited, total):
    global answer
    if len(visited) == N+1:
        answer += total
        return
    for i in range(4):
        nx = x + delta[i][0]
        ny = y + delta[i][1]

        if [nx, ny] not in visited:
            visited.append([nx,ny])
            dfs(nx, ny, visited, total * prob[i])
            visited.pop()

if __name__ == "__main__":
    N, ep, wp, sp, np, = map(int, sys.stdin.readline().split())
    prob = [ep, wp, sp, np]
    answer = 0

    dfs(0, 0, [[0, 0]], 1)

    print(answer * (0.01 ** N))