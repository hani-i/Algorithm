import sys

if __name__ == '__main__':
     array = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
     word = sys.stdin.readline().rstrip("/n")
     time = 0
     for i in word:
          for j in array:
               if j.find(i)!=-1:
                    time += array.index(j)+3
     print(time)