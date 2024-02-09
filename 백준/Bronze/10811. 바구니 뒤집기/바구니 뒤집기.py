import sys

if __name__ == '__main__':
    N,M = map(int, sys.stdin.readline().split())
    array = [i for i in range(1,N+1)]
    for _ in range(M):
        i,j = map(int, sys.stdin.readline().split())
        tmp = array[i-1:j]
        tmp.reverse()
        
        tmp_idx=0
        for idx in range(i-1,j):
           array[idx] = tmp[tmp_idx]
           tmp_idx += 1

    print(*array,sep=" ")