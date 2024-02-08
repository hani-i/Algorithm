
import sys

if __name__ == '__main__':
    N,M = map(int, sys.stdin.readline().split())
    array=[0 for i in range(N)] #크기지정

    for i in range(0,N):
        array[i]=i+1

    for _ in range(M):
        x,y = map(int, sys.stdin.readline().split())
        array[x-1],array[y-1] = array[y-1],array[x-1]

for a in array:
    print(a,end=' ')
