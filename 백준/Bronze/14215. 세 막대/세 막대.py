import sys


if __name__ == '__main__':
    a, b, c = map(int, sys.stdin.readline().split())

    MAX = max(a, b, c)
    SUM = (a+b+c) - MAX #가장 긴 변을 제외한 두 변의 합

    if MAX < SUM:
        print(a+b+c)
    else:
        MAX = SUM-1
        print(MAX + SUM)
