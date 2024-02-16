import sys

if __name__ == '__main__':
    N = 9
    MAX = 0
    row = 0
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    for i in range(N):
        if MAX < max(A[i]):
            MAX = max(A[i])
            row = i

    print(MAX)
    print(row+1,A[row].index(MAX)+1)