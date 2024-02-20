import sys
from math import floor

if __name__ == '__main__':
    N, B = map(int,sys.stdin.readline().rstrip('\n').split())
    num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    div = ''

    while N!=0:
        value = num[N%B]
        div += value #나머지
        N = N//B #몫

    print(''.join(reversed(div)))





