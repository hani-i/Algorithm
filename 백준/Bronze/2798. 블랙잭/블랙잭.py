import sys
from itertools import combinations

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    myList = list(map(int, sys.stdin.readline().split()))
    comList = list(combinations(myList, 3))
    max = 0

    for i in range(len(comList)):
        SUM = sum(comList[i]) # sum : 리스트, 튜플 등 반복 가능한 객체의 모든 요소를 더한 값
        if max < SUM <= M:
           max = SUM

    print(max)
