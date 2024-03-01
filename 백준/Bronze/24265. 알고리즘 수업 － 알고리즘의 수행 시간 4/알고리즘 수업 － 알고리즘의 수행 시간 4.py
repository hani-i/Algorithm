import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    sum = 0

    for i in range(2,n+1):
        sum += i-1

    print(sum)
    print(2)
