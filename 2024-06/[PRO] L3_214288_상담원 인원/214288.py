import sys
from heapq import heappush, heappop
from itertools import combinations_with_replacement, permutations


def cal(waiting, num):
    total = 0
    consultant = []
    for _ in range(num):
        heappush(consultant, 0)
    for start, end in waiting:
        tmp = heappop(consultant)
        if start > tmp:
            heappush(consultant, end)
        else:
            wait_time = tmp - start
            total += wait_time
            heappush(consultant, end + wait_time)
    return total


def solution(k, n, reqs):
    answer = sys.maxsize
    waiting = [[] for _ in range(k + 1)]
    for req in reqs:
        waiting[req[2]].append((req[0], req[0] + req[1]))
    cases = set()
    for comb in combinations_with_replacement([i for i in range(1, n - k + 2)], r=k):
        if sum(comb) == n:
            for perm in permutations(comb, k):
                cases.add(perm)

    for case in cases:
        time = 0
        for i in range(k):
            time += cal(waiting[i + 1], case[i])
        answer = min(answer, time)

    return answer