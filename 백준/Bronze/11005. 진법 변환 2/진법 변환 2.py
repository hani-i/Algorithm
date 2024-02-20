import sys

if __name__ == '__main__':
    N, B = map(int, input().split())
    s = ''
    arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while N:
        s += str(arr[N % B])
        N //= B

    print(s[::-1])
    





