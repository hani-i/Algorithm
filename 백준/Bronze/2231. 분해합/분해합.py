import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())

    for i in range(1, N+1):
        myStr = str(i)
        myList = []
        SUM = 0
        
        for m in myStr:
            myList.append(m)
            SUM += int(m)

        if i+SUM == N:
            print(i)
            break

        elif i == N:
            print(0)

