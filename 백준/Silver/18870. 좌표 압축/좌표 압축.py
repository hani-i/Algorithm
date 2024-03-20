
import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    myList = list(map(int, sys.stdin.readline().split()))

    #중복을 없애 리스트를 만든 후, 이 값을 딕셔너리의 키로 만든다. 
    arr = sorted(set(myList))
    myDict = {}
    for i in range(len(arr)):
        myDict[arr[i]] = i

    for i in myList:
        print(myDict[i], end=" ")
