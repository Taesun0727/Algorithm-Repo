import sys
from collections import deque
sys.stdin = open('../../input.txt')

def move(start, end):
    queue = deque()
    visited = [True] * (N + 1)
    visited[start] = False
    queue.append((start, []))

    while queue:
        cur, route = queue.popleft()
        if cur == end:
            for i in range(1, len(route)+1):
                have_milk[route[i-1]] += i
            else:
                return

        for next in tree[cur]:
            if visited[next]:
                visited[next] = False
                queue.append((next, route+[next]))

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    tree = [[] for _ in range(N+1)]
    have_milk = [0] * (N+1)
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)

    Q = int(sys.stdin.readline())

    for _ in range(Q):
        arr = list(map(int, sys.stdin.readline().split()))
        if arr[0] == 1:
            move(arr[1], arr[2])
        if arr[0] == 2:
            print(have_milk[arr[1]])