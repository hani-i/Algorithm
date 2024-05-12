import sys
import copy
from collections import deque
sys.setrecursionlimit(100000)
from collections import deque

t = int(input())
arr = [list(input()) for _ in range(t)]
arr2 = copy.deepcopy(arr)

color = ['R','G','B']
ans1=0
ans2=0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(array,c,x,y):
    que = deque()
    que.append((x,y))

    while que:
        a,b = que.popleft()
        for i in range(4):
            newx = a+dx[i]
            newy =b+dy[i]

            if 0<=newx and 0<=newy and newx<t and newy<t and array[newx][newy]==c:
                array[newx][newy]='O'
                que.append((newx, newy))


for i in range(t):
    for j in range(t):
        if arr[i][j] in color:
            ans1+=1
            dfs(arr,arr[i][j],i,j)

print(ans1)

for i in range(t):
    for j in range(t):
        if arr2[i][j] == 'G':
            arr2[i][j] ='R'


for i in range(t):
    for j in range(t):
        if arr2[i][j] in color:
            ans2+=1
            dfs(arr2,arr2[i][j],i,j)

print(ans2)