import sys

sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    answer = []

    for i in range(1, N):
        answer.append(arr[i]-arr[i-1])

    answer.sort(reverse=True)

    print(sum(answer[M-1:]))