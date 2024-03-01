import sys


if __name__ == '__main__':

    N = int(sys.stdin.readline())
    xList = []
    yList = []

    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        xList.append(x)
        yList.append(y)

    print((max(xList)-min(xList)) * (max(yList)-min(yList)))

