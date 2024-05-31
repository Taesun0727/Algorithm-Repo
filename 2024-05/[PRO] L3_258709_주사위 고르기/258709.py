from itertools import combinations
from itertools import product
import bisect
import sys


def solution(dice):
    answer = []
    dice_len = len(dice)
    max_win = -sys.maxsize
    check = []

    for comb in combinations([i for i in range(dice_len)], dice_len // 2):
        first_team = []
        second_team = []
        sum_first_team = []
        sum_second_team = []

        for i in range(dice_len):
            if i not in comb:
                second_team.append(i)
            else:
                first_team.append(i)

        check.append(first_team)
        check.append(second_team)

        for pro in product([i for i in range(6)], repeat=dice_len // 2):
            first_tmp = 0
            second_tmp = 0
            for i in range(len(pro)):
                first_tmp += dice[first_team[i]][pro[i]]
                second_tmp += dice[second_team[i]][pro[i]]
            sum_first_team.append(first_tmp)
            sum_second_team.append(second_tmp)

        sum_first_team.sort()
        sum_second_team.sort()
        win = 0
        lose = 0

        for num in sum_first_team:
            win += bisect.bisect(sum_second_team, num - 1)

        if win > max_win:
            max_win = win
            answer = first_team

    for i in range(len(answer)):
        answer[i] += 1

    return answer