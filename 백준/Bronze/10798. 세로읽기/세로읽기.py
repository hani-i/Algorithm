import sys

if __name__ == '__main__':
    N = 5
    length = 0
    A = [list(sys.stdin.readline().rstrip()) for i in range(N)]

    for i in range(5):
        if length < len(A[i]):
            length = len(A[i])

    for i in range(length):
        for j in range(N):
            try:
                if A[j][i] !=None:
                    print(A[j][i],end="")
            except:
                pass


    