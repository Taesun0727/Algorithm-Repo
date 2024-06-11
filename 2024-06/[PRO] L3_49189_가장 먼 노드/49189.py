from collections import deque

visited = []
graph = []

def bfs():
    global visited
    visited[1] = 1
    queue = deque()
    queue.append((1, 0))

    while queue:
        cur, count = queue.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = count + 1
                queue.append((nxt, count + 1))

def solution(n, edge):
    global visited, graph
    answer = 0
    visited = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    bfs()
    max_value = max(visited)
    for value in visited:
        if value == max_value:
            answer += 1
    return answer