import sys
from collections import deque
sys.stdin = open('../../input.txt')

def bfs(num):
    global answer, cnt
    queue = deque([num])
    while queue:
        cur = queue.popleft()
        if cur == M:
            answer = dis[cur]
            cnt += 1
            continue
        for nx in [cur-1, cur+1, cur*2]:
            if 0 <= nx < 100001 and (dis[nx] == 0 or dis[nx] == dis[cur]+1):
                dis[nx] = dis[cur] + 1
                queue.append(nx)

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    dis = [0] * 100001
    answer, cnt = 0, 0
    bfs(N)
    print(answer)
    print(cnt)
