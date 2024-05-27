from collections import defaultdict


def solution(topping):
    answer = 0
    dic = [0] * 10001
    first_set = set()
    second_set = set()
    for num in topping:
        dic[num] += 1
        second_set.add(num)

    for num in topping:
        first_set.add(num)
        if dic[num] == 1:
            second_set.remove(num)
        dic[num] -= 1
        if len(first_set) == len(second_set):
            answer += 1

    return answer