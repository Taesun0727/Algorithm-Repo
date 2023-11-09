import sys
from itertools import combinations
sys.stdin = open('../../input.txt')


if __name__ == "__main__":
    S = list(map(str, sys.stdin.readline().rstrip()))
    stack = []
    tmp = []

    for i in range(len(S)):
        if S[i] == "(":
            stack.append(i)
        elif S[i] == ")":
            tmp.append((stack.pop(), i))

    results = set()
    for i in range(1, len(tmp) + 1):
        c = combinations(tmp, i)

        for x in c:
            new_s = list(S)
            for j in x:
                new_s[j[0]] = ""
                new_s[j[1]] = ""
            results.add("".join(new_s))

    for result in sorted(list(results)):
        print(result)
