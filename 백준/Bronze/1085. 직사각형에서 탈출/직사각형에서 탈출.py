import sys


if __name__ == '__main__':
    x, y, w, h = map(int, sys.stdin.readline().split())
    wx = w - x
    hy = h - y

    list = [x, y, wx, hy]
    print(min(list))



