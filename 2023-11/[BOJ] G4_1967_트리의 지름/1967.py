import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('../../input.txt')

def dfs(num, cost):
    for x in tree[num]:
        next, cos = x
        if dis[next] == -1:
            dis[next] = cost + cos
            dfs(next, dis[next])


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b, cost = map(int, sys.stdin.readline().split())
        tree[a].append((b, cost))
        tree[b].append((a, cost))

    dis = [-1] * (N+1)
    dis[1] = 0
    dfs(1, 0)

    start = dis.index(max(dis))
    dis = [-1] * (N+1)
    dis[start] = 0
    dfs(start, 0)

    print(max(dis))