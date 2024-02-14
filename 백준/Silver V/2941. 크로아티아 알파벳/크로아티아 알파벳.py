import sys

if __name__ == '__main__':
     al = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
     x = sys.stdin.readline().rstrip('\n')

     for i in al:
          if i in x:
               x = x.replace(i, "_")

     print(len(x))