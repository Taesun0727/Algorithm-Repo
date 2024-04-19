import sys
sys.stdin = open('../../input.txt')

def solve(num):
    cnt = 1
    max_num, min_num = arr[0], arr[0]
    for i in range(1, N):
        max_num = max(max_num, arr[i])
        min_num = min(min_num, arr[i])
        if max_num - min_num > num:
            cnt += 1
            max_num = arr[i]
            min_num = arr[i]
    return cnt

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    start, end = 0, max(arr)
    answer = 0
    while start <= end:
        mid = (start + end ) // 2
        if solve(mid) <= M:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1

    print(answer)