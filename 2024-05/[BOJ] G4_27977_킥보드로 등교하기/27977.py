import sys
sys.stdin = open('../../input.txt')

def check(num):
    cur, status = 0, num
    charge = 0
    for i in range(N+1):
        tmp = chargers[i]
        dis = chargers[i] - cur
        if status < dis:
            if num < dis:
                return False
            else:
                charge += 1
                status = num - dis
                cur = tmp
        else:
            status = status - dis
            cur = tmp
        if charge > K:
            return False

    return True


if __name__ == "__main__":
    L, N, K = map(int, sys.stdin.readline().split())
    chargers = list(map(int, sys.stdin.readline().split())) + [L]
    chargers.sort()

    start, end = 1, L

    while start <= end:
        mid = (start + end) // 2

        if check(mid):
            end = mid - 1
        else:
            start = mid + 1

    print(start)