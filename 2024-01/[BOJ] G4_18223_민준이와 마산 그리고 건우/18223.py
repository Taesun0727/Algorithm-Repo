import sys
from heapq import heappop, heappush
sys.stdin = open('../../input.txt')

def dijkstra(start, end):
    heap = []
    heappush(heap, (0, start))
    dp = [sys.maxsize] * (N + 1)
    dp[start] = 0

    while heap:
        value, current = heappop(heap)
        for next, next_value in graph[current]:
            if dp[next] > value + next_value:
                dp[next] = value + next_value
                heappush(heap , (dp[next], next))

    return dp[end]


if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    if dijkstra(1, N) == dijkstra(1, K) + dijkstra(K, N):
        print("SAVE HIM")
    else:
        print("GOOD BYE")