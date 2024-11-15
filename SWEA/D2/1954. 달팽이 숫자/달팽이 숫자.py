
vector = [(0,1), (1,0), (0,-1), (-1,0)]
T = int(input())

for t in range(1,T+1):
    x = y = 0
    vectorIdx = 0
    N = int(input())
    array = [[0]*N for _ in range(N)]
    array[0][0]=1
    for number in range(2, N*N+1):
        newX =x + vector[vectorIdx][0]
        newY =y + vector[vectorIdx][1]
        
        if N<=newX or N<=newY or newX<0 or newY<0 or array[newX][newY]!=0 :
            vectorIdx = (vectorIdx +1)% 4
            newX =x + vector[vectorIdx][0]
            newY =y + vector[vectorIdx][1] 
        x = newX
        y = newY
        array[x][y] = number
    print('#'+str(t))
    for row in array:
        print(*row)
    
    
        
        
       
            
        
    