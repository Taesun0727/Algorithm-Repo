import sys
sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    N, T = map(int, sys.stdin.readline().split())
    INF = 10000
    dist = [[INF] * (N) for _ in range(N)]
    tp = [0] * N
    city = []
    for i in range(N):
        s, x, y = map(int, sys.stdin.readline().split())
        city.append((x, y))
        if s == 1:
            tp[i] = 1

    for i in range(N):
        for j in range(N):
            if i == j:
                dist[i][j] = 0
                continue
            distance = abs(city[i][0] - city[j][0]) + abs(city[i][1] - city[j][1])
            if tp[i] == 1 and tp[j] == 1 and T <= distance:
                dist[i][j] = T
            else:
                dist[i][j] = distance

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    M = int(sys.stdin.readline())
    for _ in range(M):
        first, second = map(int, sys.stdin.readline().split())
        print(dist[first-1][second-1])

