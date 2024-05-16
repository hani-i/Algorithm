T = int(input())

dicvalue = dict() #좌표로 값
dicidx = dict() #값으로 좌표
dicvalue[(1,1)] = 1
dicidx[(1)] = (1,1)

fx = 1
fy = 2
for i in range(2,45000):

    if fy==0:
        fy = fx
        fx = 1

    dicvalue[(fx,fy)] = i
    dicidx[i] = (fx,fy)

    fx += 1
    fy -=1

for t in range(T):
    x, y = map(int,input().split())
    tup1 = dicidx[x]
    tup2 = dicidx[y]
    #print(tup1,tup2)
    nx = tup1[0]+tup2[0]
    ny = tup1[1] + tup2[1]
    #print(nx,ny)
    print(f'#{t+1} {dicvalue[(nx,ny)]}')




