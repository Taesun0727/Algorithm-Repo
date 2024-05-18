import sys

def solution(sequence, k):
    answer = []
    start, end = 0, 0
    cur = sequence[start]
    min_len = sys.maxsize
    while True:
        if cur <= k:
            if cur == k:
                tmp = end - start
                if min_len > tmp:
                    min_len = tmp
                    answer = [start, end]
                elif min_len == tmp and start < answer[0]:
                    answer = [start, end]
            end += 1
            if end == len(sequence):
                break
            cur += sequence[end]
        elif cur > k:
            cur -= sequence[start]
            start += 1

    return answer