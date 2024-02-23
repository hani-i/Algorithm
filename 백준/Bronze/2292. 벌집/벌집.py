import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip('/n'))
    FIRST = 2
    idx = 1

    while FIRST<=N:
        FIRST += 6*idx
        idx+=1

    print(idx)
