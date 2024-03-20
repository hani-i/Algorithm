
import sys

if __name__ == '__main__':

    N = int(sys.stdin.readline())
    myList = []
    for i in range(N):
        a,b = sys.stdin.readline().split()
        myList.append((int(a), b))

    myList.sort(key=lambda x: x[0])
    for m in myList:
        print(m[0], m[1])





