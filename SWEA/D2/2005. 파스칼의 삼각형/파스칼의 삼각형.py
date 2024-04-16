T = int(input())

for t in range(T):
    N = int(input())
    myList = [0]*(N)
    printList = [0]*(N)
    tmp = []
    count = 1 #원소 수+1
    #줄
    print(f'#{t+1} ')
    
    for i in range(N):
        for j in range(count):
            if j == 0 or j==i:
                myList[j] = 1
                printList[j] = 1
                #print("1 값")
                if j==i:
                    myList = printList[:]
            else :
                printList[j] = myList[j-1] + myList[j]
        print(*printList[0:count], sep=" ")                
        count += 1
            
            
        
        
    