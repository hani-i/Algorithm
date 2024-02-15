import sys

if __name__ == '__main__':
     N = int(sys.stdin.readline())
     count = N

     for n in range(N):
         x = sys.stdin.readline().rstrip('\n')
         sig = 0
         for i in range(len(x)-1):
              if x[i] != x[i+1]:
                   if x[i] in x[i+1:]:
                        sig = 1

              if sig ==1:
                  count-=1
                  break

     print(count)