
import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    myList = [0 for _ in range(10001)]

    for _ in range(N):
        myList[int(sys.stdin.readline())] += 1

    for i in range(len(myList)):
        if myList[i] != 0:
            for _ in range(myList[i]):
                print(i)





