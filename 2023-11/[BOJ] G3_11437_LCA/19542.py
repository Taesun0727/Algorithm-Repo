import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('../../input.txt')

def dfs(cur, pre):
    global result
    max_value = 0
    for next in tree[cur]:
        if next != pre:
            max_value = max(max_value, dfs(next, cur))

    if max_value >= D:
        result += 1

    return max_value + 1

if __name__ == "__main__":
    N, S, D = map(int, sys.stdin.readline().split())
    tree = [[] for _ in range(N+1)]
    result = 0
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)
    dfs(S, 0)

    print(max(0, 2*(result-1)))
