import sys

if __name__ == '__main__':
    A = [[0 for i in range(100)] for _ in range(100)]
    N = int(sys.stdin.readline())
    count = 0

    for i in range(N):
        x,y = map(int, sys.stdin.readline().split())
        for j in range(x,x+10):
            for k in range(y,y+10):
                if A[j][k] == 0:
                    A[j][k] = 1
                else:
                    count+=1

    print(100*N - count)