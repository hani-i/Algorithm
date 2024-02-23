import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip('/n'))
    ini = 2

    for i in range(N):
        ini = ini*2 - 1

    print(ini**2)






