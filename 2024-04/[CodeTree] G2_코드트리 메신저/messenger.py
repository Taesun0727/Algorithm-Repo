import sys
sys.stdin = open('../../input.txt')

class Query:
    def __init__(self, cmd, t, x, name, n):
        self.cmd = cmd
        self.t = t
        self.x = x
        self.name = name
        self.n = n

    def __str__(self):
        return ( "cmd: " + str(cmd) + " t: " + str(t) + " x: " + str(x) + " name: " + name + " n: " + str(n))


if __name__ == "__main__":
    L, Q = map(int, sys.stdin.readline().split())
    queries = []
    names = set()
    p_queries = {}
    entry_time = {}
    position = {}
    exit_time = {}

    for _ in range(Q):
        command = sys.stdin.readline().split()
        cmd, t, x, n = -1, -1, -1, -1
        name = ""
        cmd = int(command[0])
        if cmd == 100:
            t, x, name = command[1:]
            t, x = map(int, [t, x])
        elif cmd == 200:
            t, x, name, n = command[1:]
            t, x, n = map(int, [t, x, n])
        else:
            t = int(command[1])
        queries.append(Query(cmd, t, x, name, n))

        if cmd == 100:
            if name not in p_queries:
                p_queries[name] = []
            p_queries[name].append(Query(cmd, t, x, name, n))
        elif cmd == 200:
            names.add(name)
            entry_time[name] = t
            position[name] = x

    for name in names:
        exit_time[name] = 0

        for q in p_queries[name]:
            time_to_removed = 0
            if q.t < entry_time[name]:
                t_sushi_x = (q.x + (entry_time[name] - q.t)) % L
                additionl_time = (position[name] - t_sushi_x + L) % L
                time_to_removed = entry_time[name] + additionl_time
            else:
                additionl_time = (position[name] - q.x + L) % L
                time_to_removed = q.t + additionl_time
            exit_time[name] = max(exit_time[name], time_to_removed)
            queries.append(Query(111, time_to_removed, -1, name, -1))

    for name in names:
        queries.append(Query(222, exit_time[name], -1, name, -1))
    queries.sort(key=lambda q: (q.t, q.cmd))
    people_num, sushi_num = 0, 0
    for i in range(len(queries)):
        if queries[i].cmd == 100:  # 초밥 추가
            sushi_num += 1
        elif queries[i].cmd == 111:  # 초밥 제거
            sushi_num -= 1
        elif queries[i].cmd == 200:  # 사람 추가
            people_num += 1
        elif queries[i].cmd == 222:  # 사람 제거
            people_num -= 1
        else:  # 사진 촬영시 답을 출력하면 됩니다.
            print(people_num, sushi_num)