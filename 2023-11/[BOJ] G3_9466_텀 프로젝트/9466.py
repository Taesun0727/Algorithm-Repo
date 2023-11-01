import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('../../input.txt')

def dfs(n):
    global result
    check[n] = True
    tmp.append(n)
    num = arr[n]
    if check[num]:
        if num in tmp:
            result += tmp[tmp.index(num):]
    else:
        dfs(num)

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        result = []
        N = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        for i in range(N):
            arr[i] -= 1
        check = [False] * N

        for i in range(N):
            if not check[i]:
                tmp = []
                dfs(i)

        print(N-len(result))