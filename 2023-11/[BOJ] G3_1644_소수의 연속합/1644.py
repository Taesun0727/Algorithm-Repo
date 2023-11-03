import sys

sys.stdin = open('../../input.txt')


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    prime = []
    prime_check = [True] * (N+1)

    for i in range(2, N+1):
        if prime_check[i]:
            prime.append(i)
        for j in range(2*i, N+1, i):
            prime_check[j] = False

    result = 0
    start, end = 0, 0
    while end <= len(prime):
        tmp = sum(prime[start:end])
        if tmp == N:
            end += 1
            result += 1
        elif tmp < N:
            end += 1
        else:
            start += 1

    print(result)