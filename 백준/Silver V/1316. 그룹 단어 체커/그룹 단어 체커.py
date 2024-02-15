import sys

if __name__ == '__main__':
     N = int(sys.stdin.readline())
     count = N

     for n in range(N):
          x = sys.stdin.readline().rstrip('\n')
          y = list(set(x))  # 중복 X
          sig = 0
          for i in y:
               min = x.find(i)
               max = x.find(i)
               for j in range(len(x)-1,-1,-1):
                    if x[j] == i:
                         max = j
                         break

               for j in range(min,max+1): #값 사이에 다른 문자가 있으면 그룹 단어 X
                    if i!=x[j]:
                         count -=1
                         sig = 1
                         break

               if sig==1:
                    break

     print(count)