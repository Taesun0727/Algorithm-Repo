from collections import deque


def solution(order):
    answer = 0
    assist = deque()
    cur = 0

    for i in range(1, len(order) + 1):
        if order[cur] != i:
            assist.insert(0, i)
        else:
            answer += 1
            cur += 1
            while assist:
                if order[cur] == assist[0]:
                    answer += 1
                    cur += 1
                    assist.popleft()
                else:
                    break

    return answer