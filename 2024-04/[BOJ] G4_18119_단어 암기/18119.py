import sys
sys.stdin = open('../../input.txt')

def words_count():
    count = 0
    for word in words:
        if know_char & word == word:
            count += 1

    print(count)

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    words = [0 for _ in range(N)]

    for i in range(N):
        word = sys.stdin.readline().strip()
        for c in word:
            words[i] |= 1 << ord(c) - 97

    know_char = (1 << 26) - 1

    for _ in range(M):
        num, spell = sys.stdin.readline().split()
        idx = ord(spell) - 97

        if num == '1':
            know_char &= ~(1 << idx)
        elif num == '2':
            know_char |= (1 << idx)

        words_count()

    ## https://studyandwrite.tistory.com/445
    ## https://westmino.tistory.com/66