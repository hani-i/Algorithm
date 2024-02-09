import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    M = max(array)
    for i in range(0,N):
        array[i] = array[i]/M*100

    print(sum(array)/N)