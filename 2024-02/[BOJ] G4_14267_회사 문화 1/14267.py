import sys
sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    emp = list(map(int, sys.stdin.readline().split()))
    stamp = [0] * (N+1)

    for _ in range(M):
        i, w = map(int, input().split())
        stamp[i] += w

    for i in range(2, N+1):
        stamp[i] += stamp[emp[i - 1]]

    stamp.pop(0)

    print(*stamp)