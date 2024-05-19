def take_minerals():
    global answer, global_picks

    for mineral in global_new_minerals:
        diamond, iron, stone = mineral

        for i in range(len(global_picks)):
            if global_picks[i] == 0:
                continue
            global_picks[i] -= 1
            if i == 0:
                answer += diamond + iron + stone
            elif i == 1:
                answer += diamond * 5 + iron + stone
            else:
                answer += diamond * 25 + iron * 5 + stone
            break


def make_new_minerals():
    global global_new_minerals
    minerals_count = len(global_minerals)
    global_new_minerals = [[0, 0, 0] for _ in range(minerals_count // 5 + 1)]

    for i in range(minerals_count):
        index = i // 5
        if global_minerals[i] == "diamond":
            global_new_minerals[index][0] += 1
        elif global_minerals[i] == "iron":
            global_new_minerals[index][1] += 1
        else:
            global_new_minerals[index][2] += 1


def cut_minerals():
    global global_picks, global_minerals
    jewel_count = 0
    for pick in global_picks:
        jewel_count += pick
    if len(global_minerals) > jewel_count * 5:
        global_minerals = global_minerals[:jewel_count * 5]

    return


def solution(picks, minerals):
    global global_picks, global_minerals, global_new_minerals, answer
    global_picks = picks
    global_minerals = minerals

    cut_minerals()
    make_new_minerals()
    global_new_minerals.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    answer = 0
    take_minerals()

    return answer