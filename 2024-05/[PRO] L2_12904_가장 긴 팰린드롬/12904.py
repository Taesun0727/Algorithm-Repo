def solution(s):
    answer = 0

    for i in range(len(s)):
        for j in range(len(s) + 1, 1, -1):
            if len(s[i:j]) <= answer:
                break
            if s[i:j] == s[i:j][::-1]:
                answer = max(answer, len(s[i:j]))

    return answer