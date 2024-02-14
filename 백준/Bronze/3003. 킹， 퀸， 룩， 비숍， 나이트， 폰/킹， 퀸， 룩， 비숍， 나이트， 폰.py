import sys

if __name__ == '__main__':
     black = [1, 1, 2, 2, 2, 8]
     x = list(map(int, sys.stdin.readline().split()))

     for i in range(len(black)):
          print(black[i]-x[i], end=" ")