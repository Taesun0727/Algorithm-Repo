def check(times, cur):
    tmp = 0
    for time in times:
        tmp += cur // time

    return tmp


def solution(n, times):
    answer = 0
    times.sort()
    start, end = times[0], times[-1] * n
    while start <= end:
        mid = (start + end) // 2
        if check(times, mid) < n:
            start = mid + 1
        else:
            end = mid - 1

    return start