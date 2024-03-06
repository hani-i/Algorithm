import sys


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    myList = list(map(int, sys.stdin.readline().split()))
    comList =[]
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                value = myList[i] + myList[j] + myList[k]
                if value <= M:
                    comList.append(value)

    print(max(comList))




