import sys
from itertools import combinations

sys.stdin = open('../../input.txt')


if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for i in range(T):
        S = list(sys.stdin.readline().rstrip())

        if S == S[::-1]:
            print(0)
            continue

        left = 0
        right = len(S)-1
        check = False

        while left < right:
            if S[left] == S[right]:
                left += 1
                right -= 1
                continue
            else:
                if S[left+1:right+1] == S[left+1:right+1][::-1]:
                    check = True
                if S[left:right] == S[left:right][::-1]:
                    check = True
                break

        if check:
            print(1)
        else:
            print(2)