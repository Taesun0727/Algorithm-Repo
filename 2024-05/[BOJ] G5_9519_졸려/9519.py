import sys
sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    N = sys.stdin.readline().rstrip()
    len_N = len(N)
    half_N = N[:(len_N + 1) // 2]

    if N == "9" * len_N:
        print(int(N) + 2)
    elif len_N == 1:
        print(int(N) + 1)
    elif len_N % 2 == 0:
        tmp = half_N + half_N[::-1]
        if int(tmp) > int(N):
            print(tmp)
        else:
            tmp = str(int(half_N) + 1)
            tmp = tmp[:] + tmp[::-1]
            print(tmp)
    else:
        tmp = half_N + half_N[-2::-1]
        if int(tmp) > int(N):
            print(tmp)
        else:
            tmp = str(int(half_N) + 1)
            tmp = tmp[:] + tmp[-2::-1]
            print(tmp)