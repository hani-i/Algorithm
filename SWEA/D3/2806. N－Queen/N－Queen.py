T = int(input())

def dfs(x):
    	global count
    	if x == N:
            count +=1
            return
        
    	for j in range(N):
            if v1[j] ==0 and v2[x+j]==0 and v3[x-j+N-1] ==0 :
                v1[j] =1
                v2[x+j]=1
                v3[x-j+N-1] =1
                
                dfs(x+1)
                
                v1[j] =0
                v2[x+j]=0
                v3[x-j+N-1] =0
    
for t in range(T):
    N = int(input())
    v1 = [0]*N
    v2 = [0]*2*N
    v3 = [0]*2*N
    count = 0 
    dfs(0)
    
    print(f'#{t+1} {count}')
    