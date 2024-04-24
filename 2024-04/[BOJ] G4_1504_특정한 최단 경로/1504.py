import sys
from heapq import heappush, heappop
sys.stdin = open('../../input.txt')

def dijkstra(start):
    heap = []
    distance = [INF] * (N+1)
    heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        count, cur = heappop(heap)
        if distance[cur] < count:
            continue
        for next, next_count in board[cur]:
            tmp = count + next_count
            if distance[next] > tmp:
                distance[next] = tmp
                heappush(heap, (count+next_count, next))

    return distance

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    board = [[]for _ in range(N+1)]
    INF = sys.maxsize

    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        board[a].append((b, c))
        board[b].append((a, c))

    v1, v2 = map(int, sys.stdin.readline().split())
    start_distance = dijkstra(1)
    v1_distance = dijkstra(v1)
    v2_distance = dijkstra(v2)
    answer = min(start_distance[v1]+v1_distance[v2]+v2_distance[N], start_distance[v2]+v2_distance[v1]+v1_distance[N])

    if answer < INF:
        print(answer)
    else:
        print(-1)