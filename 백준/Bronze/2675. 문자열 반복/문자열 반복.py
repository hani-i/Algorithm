import sys

if __name__ == '__main__':
     T = int(sys.stdin.readline())
     for i in range(T):
          x,y = (sys.stdin.readline().rstrip()).split()
          x = int(x)
          for j in y:
               for k in range(x):
                    print(j,end="")
          print()