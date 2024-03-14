
import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    STR = str(N)
    myList = [int(s) for s in STR]

    myList.sort(reverse=True)
    print(*myList,sep='')




