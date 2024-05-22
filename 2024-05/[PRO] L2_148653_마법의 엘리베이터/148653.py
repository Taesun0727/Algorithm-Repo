def solution(storey):
    answer = 0

    while storey:
        remain = storey % 10

        if remain > 5:
            answer += 10 - remain
            storey += 10
        elif remain < 5:
            answer += remain
        else:
            if storey // 10 % 10 > 4:
                storey += 10
            answer += remain

        storey //= 10

    return answer