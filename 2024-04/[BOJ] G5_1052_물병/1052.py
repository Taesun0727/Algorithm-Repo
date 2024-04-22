import sys

sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    count = 0

    while bin(N).count('1') > M:
        N += 1
        count += 1

    print(count)