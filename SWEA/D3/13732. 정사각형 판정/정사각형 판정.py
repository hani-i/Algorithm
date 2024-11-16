import math 

direction = [(0,-1),(0,1),(-1,0),(1,0)]

def check1(number):
    sqrtnumber = (int)(math.sqrt(number))

    if sqrtnumber*sqrtnumber == number:
        return True
    return False

def check2(N,graph,coor):
    for c in coor:
        x,y = c
        count = 0
        for dic in direction:
            newX  = x+dic[0]
            newY  = y+dic[1]
            
            if(0<=newX<N and 0<=newY<N):
                if graph[newX][newY] =='#':
                    count += 1
                    continue
        if count<2:
            return False
    return True
        
T = int(input())

for t in range(1,T+1) : 
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(input()))
    
    # #카운트
    count = 0
    #좌표 저장
    coor = []
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] == '#':
                count += 1
                coor.append((i,j))
                
    #정사각형을 이룰 수 있는 수면 인접한 갯수가 2개 이상인지
    if(count ==1):
        print(f'#{t} yes')  
    elif(check1(count) and check2(N,graph,coor)):
        print(f'#{t} yes')
    else : print(f'#{t} no')
        
            
            
        
                
    
        