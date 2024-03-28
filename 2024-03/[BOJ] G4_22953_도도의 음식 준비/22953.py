import sys
sys.stdin = open('../../input.txt')

def isPossible(value):
    cnt = 0
    for num in arr:
        cnt += value // num

    return M <= cnt

def binary_search():
    left, right = 1, 1e13

    while left <= right:
        mid = (left + right) // 2
        if isPossible(mid):
            right = mid - 1
        else:
            left = mid + 1

    return int(left)

def dfs(idx, cnt):
    global answer

    answer = min(answer, binary_search())
    if cnt == K:
        return

    for i in range(idx, N):
        if 1 < arr[i]:
            arr[i] -= 1
            dfs(i, cnt+1)
            arr[i] += 1

if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    answer = 1e13
    dfs(0, 0)

    print(answer)