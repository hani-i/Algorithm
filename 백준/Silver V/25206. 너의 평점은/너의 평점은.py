import sys


if __name__ == '__main__':

     grade = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
     score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
     totalScore = 0 #학점의 총합
     total = 0
     for i in range(20):
          x,y,z = (sys.stdin.readline()).rstrip().split()
          y = float(y)
          if z=='P':
               pass
          else:
               totalScore += y
               total+= y * score[grade.index(z)]

     print(total/totalScore)