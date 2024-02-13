import sys

if __name__ == '__main__':
     T = sys.stdin.readline().rstrip()
     count = T.count(" ")+1

     if T.find(" ")==0:
          count-=1

     if T.find(" ")==len(T)-1:
          count-=1

     print(count)