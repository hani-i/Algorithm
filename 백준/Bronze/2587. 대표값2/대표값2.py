import sys


if __name__ == '__main__':
    myList = []

    for _ in range(5):
        myList.append(int(sys.stdin.readline()))

    myList.sort()
    print(sum(myList)//5)
    print(myList[2])



