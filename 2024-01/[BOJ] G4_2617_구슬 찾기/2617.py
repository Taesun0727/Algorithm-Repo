import sys
sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    graph = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = 1

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

    answer = 0

    for i in range(1, N+1):
        light = 0
        heavy = 0

        for j in range(1, N+1):
            if graph[i][j]:
                light += 1
            if graph[j][i]:
                heavy += 1

        if light > N // 2 or heavy > N // 2:
            answer += 1

    print(answer)