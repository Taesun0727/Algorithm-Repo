def solution(plans):
    answer = []
    play = []
    stop = []

    for plan in plans:
        name, start, playtime = plan
        start = list(map(int, start.split(":")))
        play.append((start[0] * 60 + start[1], int(playtime), name))

    play.sort()

    for i in range(len(plans)):
        c_start, c_playtime, c_name = play[i]
        if i == len(plans) - 1:
            stop.append((c_playtime, c_name))
            break
        n_start, n_playtime, n_name = play[i + 1]
        if c_start + c_playtime <= n_start:
            answer.append(c_name)
            c_start = c_start + c_playtime
            while stop:
                r_time, r_name = stop.pop()
                if c_start + r_time <= n_start:
                    c_start += r_time
                    answer.append(r_name)
                else:
                    stop.append((c_start + r_time - n_start, r_name))
                    break
        else:
            r_time = (c_start + c_playtime) - n_start
            stop.append((r_time, c_name))

    while stop:
        answer.append(stop.pop()[-1])

    return answer