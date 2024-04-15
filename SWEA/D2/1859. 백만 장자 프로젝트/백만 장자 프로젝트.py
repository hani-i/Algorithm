re = int(input())

for r in range(re):
    x = int(input())
    revenue = 0
    myList = list(map(int, input().split()))
    mymax = myList[x-1]
    
    for i in range(x-2, -1, -1):
        if mymax<myList[i]:
            mymax = myList[i]
        elif myList[i] < mymax:
            revenue += mymax - myList[i]
    print(f'#{r+1} {revenue}')