import sys

sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = sorted(list(map(int, sys.stdin.readline().split())))

    min_value = sys.maxsize
    result = []

    for i in range(N-2):
        cur = arr[i]
        start, end = i+1, N-1

        while start < end:
            cur_sum = cur + arr[start] + arr[end]

            if abs(cur_sum) < min_value:
                result = [cur, arr[start], arr[end]]
                min_value = abs(cur_sum)
            if cur_sum < 0:
                start += 1
            elif cur_sum > 0:
                end -= 1
            else:
                break

    print(*result)