import sys

sys.stdin = open('../../input.txt')


if __name__ == "__main__":
    N, L = map(int, sys.stdin.readline().split())
    water = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    answer = 0
    water.sort(key = lambda x : (x[0], x[1]))
    cur = 0
    for i in range(N):
        start, end = water[i]
        if cur > end:
            continue
        if cur < start:
            cur = start
        mok = (end - cur) // L
        if (end - cur) % L > 0:
            mok += 1
        cur += L * mok
        answer += mok

    print(answer)
