from heapq import heappop, heappush

def solution(n, k, enemy):
    answer = 0
    heap = []
    cur = 0
    for e in enemy:
        heappush(heap, -e)
        cur += e

        if cur > n:
            if k == 0:
                break
            cur += heappop(heap)
            k -= 1

        answer += 1

    return answer