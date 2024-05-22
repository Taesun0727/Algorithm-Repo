def solution(x, y, n):
    answer = 0
    s = set()
    s.add(x)

    while s:
        if y in s:
            return answer
        nx = set()

        for num in s:
            if num + n <= y:
                nx.add(num + n)

            if num * 2 <= y:
                nx.add(num * 2)

            if num * 3 <= y:
                nx.add(num * 3)

        s = nx
        answer += 1

    return -1