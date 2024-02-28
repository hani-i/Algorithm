import math
import sys

if __name__ == '__main__':
    A, B, V = map(int, sys.stdin.readline().split())
    diff = (V-A)/(A-B)
    day = math.ceil(diff)

    print(day+1)