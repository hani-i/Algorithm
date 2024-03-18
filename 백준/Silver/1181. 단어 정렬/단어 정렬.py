
import sys

if __name__ == '__main__':

    N = int(sys.stdin.readline())
    mySet = set()

    for _ in range(N):
        mySet.add(sys.stdin.readline().rstrip())

    myList = list(mySet)
    myList.sort(key=lambda x: (len(x), x))

    print(*myList, sep="\n")

