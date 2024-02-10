import sys

if __name__ == '__main__':
     str = sys.stdin.readline().rstrip('\n')
     array = [-1 for i in range(26)]

     for i in range(len(str)):
          idx = (ord(str[i]) - 97)
          if array[idx] ==-1:
               array[idx] = i

     print(*array)