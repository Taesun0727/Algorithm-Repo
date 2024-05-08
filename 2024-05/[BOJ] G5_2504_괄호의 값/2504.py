import sys
sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    st = sys.stdin.readline().rstrip()
    stack = []
    tmp = 1
    answer = 0
    for i in range(len(st)):
        if st[i] == "(":
            stack.append(st[i])
            tmp *= 2
        elif st[i] == "[":
            stack.append(st[i])
            tmp *= 3
        elif st[i] == ")":
            if not stack or stack[-1] == "[":
                answer = 0
                break
            if st[i-1] == "(":
                answer += tmp
            stack.pop()
            tmp //= 2
        else:
            if not stack or stack[-1] == "(":
                answer = 0
                break
            if st[i-1] == "[":
                answer += tmp
            stack.pop()
            tmp //= 3

    if stack:
        print(0)
    else:
        print(answer)