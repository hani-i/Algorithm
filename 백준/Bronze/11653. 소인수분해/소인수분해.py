import math
import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    END = math.ceil(N/2)+1 #약수는 N/2 보다 클 수 없다는 점을 이용
    list = []
    
    if N == 1:
        print()

    else:
        while END<=N:
           for i in range(2, END):
               if N%i == 0:
                   print(i)
                   N = N/i
                   END = math.ceil(N/2)+1
                   break

           else:
               print(int(N))
               break



