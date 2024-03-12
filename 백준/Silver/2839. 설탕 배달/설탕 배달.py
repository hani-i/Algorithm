import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    count = 0

    while 0 < N:
        if N % 5 == 0:
            count = count + (N // 5)
            N = 0
            break
        else:
            N -= 3
            count +=1

    if (N != 0):
        print(-1)
    else:
        print(count)


