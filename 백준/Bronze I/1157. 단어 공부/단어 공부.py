import sys

if __name__ == '__main__':
     str = sys.stdin.readline().rstrip()
     str = str.upper()
     array = [0 for i in range(26)]

     for i in str:
          x = ord(i)
          array[x-65]+=1

     y = array.count(max(array))
     if y>1:
          print("?")

     else:
          print(chr(array.index(max(array)) + 65))