

def dfs(x, c):
    global Mymax
    #print(f'c={c}, x={x}')
    if c == count:
        Mymax = max(Mymax, int("".join(map(str, x))))
        return

    for i in range(len(x)-1):
        for j in range(i+1, len(x)):
            x[i], x[j] = x[j], x[i]
            intx = int("".join(map(str, x)))
            myList =[intx, c]
            if myList not in v: #단순히 값만 같으면 안됨. 교환횟수까지 기록해야 한다.
                v.append(myList)
                dfs(x, c+1)

            x[i], x[j] = x[j], x[i] #꼭 다시 원상복구

T = int(input())
for t in range(T):
    num, count = input().split()
    num = list(map(str, num))
    count = int(count)
    Mymax = 0 #최댓값 저장
    v = [] # 확인했던 길은 가지 않도록 가지치기
    dfs(num,0)
    print(f'#{t+1} {Mymax}')
