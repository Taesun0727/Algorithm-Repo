import sys
sys.stdin = open('../../input.txt')

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
    K = int(sys.stdin.readline())
    answer = 0

    for row in range(N):
        current_zero_count = 0
        for num in board[row]:
            if num == 0:
                current_zero_count += 1

        same_row = 0
        if current_zero_count <= K and current_zero_count % 2 == K % 2:
            for next_row in range(N):
                if board[row] == board[next_row]:
                    same_row += 1

        answer = max(answer, same_row)

    print(answer)