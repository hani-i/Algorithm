def dfs(x,y):
    global answer
    #print(x, y, "호출")
    if T<=x or T<=y or x<0 or y<0 or visited[x][y]==1:
        return
    if x==T-1 and y==T-1:
        answer+=1
        return

    if visited[x][y]==0 and answer==0:
        visited[x][y] = 1
        dfs(x+arr[x][y], y)
        dfs(x, y + arr[x][y])

T = int(input())

arr = [list(map(int, input().split()))for _ in range(T)]
visited = [[0]*T for _ in range(T)]
#print(arr)
x=0
y=0
answer = 0

dfs(x,y)

if answer ==1:
    print("HaruHaru")
else:
    print("Hing")