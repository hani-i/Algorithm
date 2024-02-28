import sys

if __name__ == '__main__':

    N, K = map(int, sys.stdin.readline().split())
    list = []
    
    #약수 insert
    for i in range(1,N+1):
        if N%i ==0:
            list.append(i)

    if len(list)<K:
        print(0)
    else:
        print(list[K-1])
