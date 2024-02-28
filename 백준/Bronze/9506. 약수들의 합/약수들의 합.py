import sys

if __name__ == '__main__':

    while True:
        X = int(sys.stdin.readline())
        list = []
        sum = 0
        
        if X==-1:
            break

        for i in range(1,X):
            if (X%i==0):
                list.append(i)
                sum += i

        if sum == X:
            print(X,'= ',end="")
            print(*list, sep=' + ')

        else:
            print(X, "is NOT perfect.")
