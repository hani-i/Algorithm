import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())

    for i in range(1, N+1):
        value = i + sum(map(int, str(i)))

        if value == N:
            print(i)
            break

        if i == N:
            print(0)
