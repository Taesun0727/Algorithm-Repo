import sys
from collections import deque

sys.stdin = open('../../input.txt')

def put_robot():
    if belt[0] > 0:
        belt[0] -= 1
        robots[0] = True

def move_robots():
    for i in range(N-2, -1, -1):
        if robots[i] and not robots[i+1] and belt[i+1] > 0:
            robots[i], robots[i+1] = False, True
            belt[i+1] -= 1
    robots[N-1] = False

def move_belt():
    belt.rotate(1)
    robots.rotate(1)
    robots[N-1] = False

def check():
    if belt.count(0) >= K:
        return True
    return False

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    belt = deque(list(map(int, sys.stdin.readline().split())))
    robots = deque([False] * N)
    answer = 0
    while True:
        answer += 1
        move_belt()
        move_robots()
        put_robot()
        if check():
            break

    print(answer)
