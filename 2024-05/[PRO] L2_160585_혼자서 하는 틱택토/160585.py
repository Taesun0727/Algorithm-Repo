def solution(book_time):
    answer = 0
    times = [0] * (24 * 60) + [0] * 10

    for bt in book_time:
        start, end = bt
        h, s = map(int, start.split(":"))
        start = h * 60 + s
        h, s = map(int, end.split(":"))
        end = h * 60 + s + 10
        times[start] += 1
        times[end] -= 1

    for i in range(1, 24 * 60 + 1):
        times[i] += times[i - 1]

    answer = max(times)

    return answer