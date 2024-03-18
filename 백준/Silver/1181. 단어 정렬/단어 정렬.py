
import sys

if __name__ == '__main__':

    N = int(sys.stdin.readline())
    myList = []

    for _ in range(N):
        myList.append(sys.stdin.readline().rstrip())

    idx = 0
    for i in range(N):
        if idx == len(myList)-1:
            break
        else:
            if myList.count(myList[idx]) >= 2:
                myList.remove(myList[idx])
            else:
                idx += 1

    myList.sort(key=lambda x: (len(x), x))

    for i in range(len(myList)):
        print(myList[i])

