import sys

if __name__ == '__main__':
    N, B = sys.stdin.readline().rstrip('\n').split()
    B = int(B)
    num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    idx = len(N)-1
    result = 0

    for i in range(len(N)):
        result += num.index(N[idx]) * B**i
        idx-=1

    print(result)
