

from collections import deque


T = int(input())

def dfs(n,x,y):
    que = deque()
    que.append((x,y))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while que:
        fx,fy = que.popleft()
        for i in range(4):
            nx = fx+dx[i]
            ny = fy + dy[i]

            if 0<=nx<N and 0<=ny<N and graph[nx][ny]== graph[fx][fy]+1:
                que.append((nx,ny))
                n += 1

    return n

for t in range(T):
    ans = 0 #방 수
    start = 0 # 출발 번호
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):

            x = dfs(1,i,j)
            if ans<x:
                ans = x # 방 수
                start = graph[i][j]
            elif ans==x and graph[i][j]<start:
                ans = x  # 방 수
                start = graph[i][j]


    print(f'#{t+1} {start} {ans}')
