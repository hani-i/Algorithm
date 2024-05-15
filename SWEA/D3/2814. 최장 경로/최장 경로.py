T = int(input())

#정점, 간선

def dfs(start,count):

    #print(start)
    global maxi
    visited[start] = 1
    maxi = max(maxi, count)

    for i in graph[start]:
        if visited[i] == 0:
            dfs(i, count+1)
    visited[start] = 0 #돌아온 후 다시 돌 수 있기 때문에 초기화해줘야 함


for t in range(T):
    maxi = 0
    n, m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n + 1)
    #print(graph)

    if m == 0:
        print(f'#{t+1} 1')
    else:
        for i in range(m):
            x, y = map(int, input().split())
            graph[x].append(y)
            graph[y].append(x)
        #print(graph)
        for k in range(1,n+1):
            visited = [0] * (n + 1)
            dfs(k,0)
        #print(visited)
        print(f'#{t + 1} {maxi+1}')

