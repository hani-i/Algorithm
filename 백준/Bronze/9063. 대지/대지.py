import sys


if __name__ == '__main__':

    N = int(sys.stdin.readline())
    xList = []
    yList = []

    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        xList.append(x)
        yList.append(y)

    maxX = max(xList)
    minX = min(xList)
    maxY = max(yList)
    minY = min(yList)

    if maxX == minX or maxY == minY:
        print(0)
    else:
        print((maxX-minX) * (maxY-minY))

