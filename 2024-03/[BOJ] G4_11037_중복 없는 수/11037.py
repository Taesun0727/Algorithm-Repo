import sys
sys.stdin = open('../../input.txt')

def check(num):
    check_num = set()
    len_num = str(num)
    for n in str(num):
        if n == '0':
            return False
        check_num.add(n)
    if len(check_num) == len(len_num):
        return True
    return False

def solve(num):
    if num >= 987654321:
        return 0
    next = num
    while True:
        next += 1
        if check(next):
            break
    return next

if __name__ == "__main__":
    while True:
        number = sys.stdin.readline().rstrip()
        if number == "":
            break
        print(solve(int(number)))