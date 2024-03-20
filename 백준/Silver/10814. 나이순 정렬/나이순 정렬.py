
import sys

if __name__ == '__main__':

    N = int(sys.stdin.readline())
    myList = []
    for i in range(N):
        INPUT = sys.stdin.readline().rstrip().split()
        myList.append([int(INPUT[0]), INPUT[1]])

    myList.sort(key=lambda x: x[0])
    for m in myList:
        print(m[0], m[1])





