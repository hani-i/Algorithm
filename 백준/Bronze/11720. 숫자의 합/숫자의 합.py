import sys

if __name__ == '__main__':
     N = int(sys.stdin.readline())
     str = sys.stdin.readline()
     sum = 0
     for i in range(N):
          sum += int(str[i])

     print(sum)