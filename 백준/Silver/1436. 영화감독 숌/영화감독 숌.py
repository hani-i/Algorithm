import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    Number = 666
    count = 0
    
    while True:
        strNumber = str(Number)

        if '666' in strNumber:
            count += 1
        if N == count:
            break

        Number += 1

    print(Number)

