
import sys

if __name__ == '__main__':

    N = int(sys.stdin.readline())
    myList = []

    for _ in range(N):
        myList.append(tuple(map(int, sys.stdin.readline().split())))

    myList.sort(key=lambda x:(x[1], x[0]))

    for i in myList:
        print(i[0], i[1])

