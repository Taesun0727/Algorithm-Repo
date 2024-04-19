import sys
sys.stdin = open('../../input.txt')

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    parent = [i for i in range(N+1)]
    cycle_count = 0
    link_count = 0
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        if find(a) == find(b):
            cycle_count += 1
        union(a, b)

    for i in range(1, N):
        if find(parent[i]) != find(parent[i+1]):
            union(i, i+1)
            link_count += 1

    print(link_count+cycle_count)