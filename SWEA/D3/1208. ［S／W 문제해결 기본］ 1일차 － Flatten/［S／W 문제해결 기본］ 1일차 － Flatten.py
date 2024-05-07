
for t in range(1,11):
    d = int(input())
    myList = list(map(int, input().split()))
    
    for _ in range(d):
        myMax = max(myList)
        myMin = min(myList)
        
        maxIdx = myList.index(myMax)
        minIdx = myList.index(myMin)
        
        myList[maxIdx] -= 1
        myList[minIdx] += 1
        #print(maxIdx, minIdx)
        
        if max(myList)-min(myList) == 0 or max(myList)-min(myList) == 1:
            break
            
    print(f'#{t} {max(myList)-min(myList)}')
        
    