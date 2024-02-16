import sys

if __name__ == '__main__':
    N = 5
    A = [list(sys.stdin.readline().rstrip()) for i in range(N)]

    for i in range(15):
        for j in range(N):
            try:
                if A[j][i] !=None:
                    print(A[j][i],end="")
            except:
                pass


    