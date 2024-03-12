import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    myList = []

    for _ in range(N):
        myList.append(int(sys.stdin.readline()))

    myList.sort()
    print(*myList, sep='\n')

