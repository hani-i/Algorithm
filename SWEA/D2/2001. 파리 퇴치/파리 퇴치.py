T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    myList = []
    for _ in range(N):
        myList.append(list(map(int, input().split())))
        
    myMax = 0
    
    for i in range(N-M+1):
        for j in range(N-M+1):
            tmp = 0
            for x in range(M):
                for y in range(M):
                    tmp += myList[i+x][j+y]        
            #print(tmp)        
            if myMax < tmp:
                myMax = tmp
    print(f'#{t+1} {myMax}')
            
        
        