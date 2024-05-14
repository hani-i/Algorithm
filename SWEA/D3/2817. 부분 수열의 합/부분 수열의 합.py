# 1
# 4 3
# 1 2 1 2


def dfs(start, summ):
    global count

    if summ==K:
        count+=1
        return
    if summ>K:
        return

    for i in range(start,N):
        dfs(i+1, summ+graph[i])

T = int(input())

for t in range(T):
    N,K = map(int, input().split())
    graph = list(map(int, input().split()))
    count = 0
    dfs(0, 0)
    print(f'#{t+1} {count}')
