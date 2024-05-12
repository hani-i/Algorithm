



from collections import deque

# def dfs(x,y):
#     if 0<=x and 0<=y and x<m and y<n and graph[x][y] == 1 and visited[x][y] == 0:
#         visited[x][y] = 1
#         graph[x][y] = 0
#         dfs(x + 1 , y)
#         dfs(x - 1, y)
#         dfs(x , y+1)
#         dfs(x, y-1)
#         dfs(x+1, y-1)
#         dfs(x + 1, y +1)
#         dfs(x -1, y + 1)
#         dfs(x -1, y -1)


def bfs(x,y):
    que = deque()
    que.append((x,y))

    while que:
        a,b = que.popleft()
        dx = [a+1,a-1,a,a,a+1,a+1,a-1,a-1]
        dy = [b, b, b+1, b-1, b-1, b+1 , b+1, b-1]
        for i in range(8):
            nx = dx[i]
            ny = dy[i]
            if 0<=nx and 0<=ny and nx<m and ny<n and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                graph[nx][ny] = 0
                que.append((nx,ny))



m, n = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(m)]
ans = 0
visited = [[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            ans += 1
            #dfs(i, j)
            bfs(i,j)

print(ans)

