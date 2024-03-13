
import sys

if __name__ == '__main__':
    N, k = map(int, sys.stdin.readline().split())
    myList = []
    myList.extend(map(int, sys.stdin.readline().split()))

    myList.sort(reverse=True)
    print(myList[k-1])













