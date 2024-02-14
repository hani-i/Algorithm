import sys

if __name__ == '__main__':
     N =int(sys.stdin.readline())
     blank = N
     star = -1
     for i in range(2*N-1):
          if i<=N-1:
               blank-=1
               star+=2

          else:
               blank += 1
               star -= 2

          print(" " * blank + "*" * star)