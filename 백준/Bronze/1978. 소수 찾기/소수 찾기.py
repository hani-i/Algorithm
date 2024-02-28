import sys

if __name__ == '__main__':

    count = 0
    N = int(sys.stdin.readline())
    list = list(map(int, sys.stdin.readline().split(" ",N-1)))
    
    for i in list:
        if i == 1:
            continue
        else:
            for j in range(2,i+1):
                if j!=i and i%j == 0:
                    break
                if j == i:
                    count += 1
    print(count)
