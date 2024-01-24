import sys

sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    dis = []

    for i in range(1, N):
        dis.append(arr[i]-arr[i-1])

    dis.sort()

    print(sum(dis[:N-M]))