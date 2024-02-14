import sys

if __name__ == '__main__':
     str = sys.stdin.readline().rstrip()

     if str==str[::-1]:
          print(1)
     else:
          print(0)