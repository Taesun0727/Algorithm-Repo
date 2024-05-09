import sys
sys.stdin = open('../../input.txt')

def mix():
    global cur, word_list
    new_word = ""
    mid = len(cur) // 2

    for i in range(mid):
        new_word += cur[i] + cur[len(cur)-1-i]

    if len(cur) % 2 != 0:
        new_word += cur[len(cur) // 2]

    cur = new_word

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    origin = sys.stdin.readline().rstrip()
    cur = origin
    word_list = [origin]
    count = 0

    while True:
        count += 1
        mix()
        if origin == cur:
            break
        word_list.append(cur)

    print(word_list[-N % len(word_list)])
