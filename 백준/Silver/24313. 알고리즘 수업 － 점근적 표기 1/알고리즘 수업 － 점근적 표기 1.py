import sys


if __name__ == '__main__':
    a1, a0 = map(int, sys.stdin.readline().split())
    c = int(sys.stdin.readline())
    n0 = int(sys.stdin.readline())

    #(a1-c)n0 + a0 <= 0
    #a1-c가 양수여서 증가함수가 되면 0보다 큰 상황이 필연적으로 발생
    if a1*n0+a0 <= c*n0 and a1<=c:
        print(1)
    else:
        print(0)




