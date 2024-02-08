import sys

if __name__ == '__main__':
    N,M = map(int, sys.stdin.readline().split())
    val = [0] * N

    for _ in range(M):
        x,y,z = map(int, sys.stdin.readline().split())

        for i in range(x,y+1):
            val[i-1] = z

for v in val:
    print(v, end=' ')