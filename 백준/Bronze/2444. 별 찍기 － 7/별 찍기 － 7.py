import sys

if __name__ == '__main__':
     N =int(sys.stdin.readline())

     for i in range(1,N):
          print(' '*(N-i) + '*'*(2*i-1))

     for i in range(N,0,-1):
          print(' '*(N-i) + '*'*(2*i-1))