import sys
sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        arr = list(map(int, sys.stdin.readline().split()))
        arr.sort()

        start, end = 0, arr[-1]

        while start <= end:
            mid = (start + end) // 2
            left = arr[0]
            count = 1

            for i in range(1, N):
                right = arr[i]

                if right - left >= mid:
                    count += 1
                    left = arr[i]

            if count >= M:
                start = mid + 1
            else:
                end = mid - 1

        print(end)
