import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('../../input.txt')

def find_depth_and_parent(cur, dep):
    visited[cur] = True
    depth[cur] = dep

    for next in tree[cur]:
        if not visited[next]:
            parent[next] = cur
            find_depth_and_parent(next, dep+1)

def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    tree = [[] for _ in range(N+1)]
    depth = [0] * (N+1)
    parent = [0] * (N+1)
    visited = [False] * (N+1)

    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)

    find_depth_and_parent(1, 0)

    M = int(sys.stdin.readline())

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        print(lca(a, b))