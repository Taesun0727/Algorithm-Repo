import sys

sys.stdin = open('../../input.txt')

def find():
    global result
    for i in range(N-1, -1, -1):
        for j in range(i+1):
            if arr[i]-arr[j] in arr_sum:
                result = arr[i]
                return

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = []
    arr_sum = set()

    for i in range(N):
        arr.append(int(sys.stdin.readline()))

    arr.sort()

    for a in arr:
        for b in arr:
            arr_sum.add(a+b)

    result = 0
    find()

    print(result)