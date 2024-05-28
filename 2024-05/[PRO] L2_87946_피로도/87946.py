global_dungeons = []
N = 0
answer = 0


def dfs(L, k, arr):
    global answer
    if answer < len(arr):
        answer = len(arr)
    if L == N:
        return

    for i in range(N):
        if i not in arr and k >= global_dungeons[i][0]:
            arr.append(i)
            k -= global_dungeons[i][1]
            dfs(L + 1, k, arr)
            arr.pop()
            k += global_dungeons[i][1]


def solution(k, dungeons):
    global global_dungeons, N
    global_dungeons = dungeons
    N = len(global_dungeons)
    dfs(0, k, [])

    return answer