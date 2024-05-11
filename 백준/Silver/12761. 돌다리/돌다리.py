
from collections import deque
def bfs(x):
    que = deque()
    que.append(x)
    graph[x] = 1

    while que:
        v = que.popleft()
        dv = [v+1, v-1, v-a, v-b, v+a, v+b, v*a, v*b]
        for i in dv:
            #if 0<=i and i<=m and graph[i]==0:
            if 0<=i<=100000 and graph[i] == 0:
                graph[i] = graph[v] + 1 #해당 배열의 값은 전에 기록된 값에서 갱신
                que.append(i)

                if i==m:
                    return graph[i]-1

#힘 a b, 시작, 끝
a, b, n, m = map(int, input().split())
graph = [0]*100001
print(bfs(n))