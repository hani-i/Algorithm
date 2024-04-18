T = int(input())
#x, y의 방향성. (오른쪽, 아래, 왼쪽, 위)
dirx = [ 0,1,0,-1 ]
diry = [ 1,0,-1,0 ]

for t in range(T):
    N = int(input())
    graph = [[0]*N for _ in range(N)]
    
    #초기위치
    x = 0
    y = -1
    
    #좌표 위치
    cur = 0
    
    num = 1
    for _ in range(N*N):
        x += dirx[cur]
        y += diry[cur]
        
        #현재 위치가 범위를 벗어나면
        if y>=N or x>= N or y<0 or x<0 or graph[x][y] != 0:
            x -= dirx[cur]
            y -= diry[cur]
            cur += 1
            if cur == 4: #범위 조정
                cur = 0
            x += dirx[cur]
            y += diry[cur]
              
        graph[x][y] = num
        if num == N*N:
            break 
        num += 1
        
    print(f'#{t+1}')
    for g in graph:
        print(*g)
        
        
        
    