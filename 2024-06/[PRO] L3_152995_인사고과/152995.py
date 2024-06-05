def solution(scores):
    answer = 0
    ho_x, ho_y, ho_sum = scores[0][0], scores[0][1], scores[0][0] + scores[0][1]
    scores.sort(key=lambda x: (-x[0], x[1]))
    max_y = 0

    for score in scores:
        x, y = score
        if ho_x < x and ho_y < y:
            return -1
        if y >= max_y:
            max_y = y
            if x + y > ho_sum:
                answer += 1

    return answer + 1