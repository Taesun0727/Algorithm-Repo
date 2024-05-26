def solution(k, tangerine):
    answer = 0
    max_value = int(10e6) + 1
    count_tangerine = [0] * max_value
    sort_tangerine = []

    for target in tangerine:
        count_tangerine[target] += 1

    for i in range(1, max_value):
        tmp = count_tangerine[i]
        if tmp != 0:
            sort_tangerine.append((tmp, i))
    sort_tangerine.sort(reverse=True)

    for num, i in sort_tangerine:
        k -= num
        answer += 1
        if k <= 0:
            break

    return answer