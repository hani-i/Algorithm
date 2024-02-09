import sys

if __name__ == '__main__':
    N,M = map(int, sys.stdin.readline().split())
    array = [i for i in range(1,N+1)]
    
    for _ in range(M):
        i,j = map(int, sys.stdin.readline().split())
        array[i-1:j]=reversed(array[i-1:j])       
        
    print(*array)