import sys

if __name__ == '__main__':

     x = sys.stdin.readline().rstrip()
     x = x.upper()
     y = list(set(x))
     co = [0 for i in range(len(y))]

     for i in range(len(y)):
          co[i]=x.count(y[i])

     if co.count(max(co))>1:
          print("?")

     else:
          print(y[co.index(max(co))])