
T = int(input())

#
def dfs(n):
    global answer
    if n == count:
        cur = "".join(num)
        cur = int(cur)
        answer = max(answer, int(cur))
        return
    for i in range(len(num)-1):
        for j in range(i+1,len(num)):
            num[i],num[j] = num[j],num[i]
            tmp = int("".join(num))

            if (tmp, n+1) not in v:
                v[(tmp,n+1)] = True
                dfs(n + 1)

            num[i],num[j] = num[j], num[i]


for t in range(T):
    answer = 0

    num,count = input().split()
    count = int(count)
    num = list(num)
    v = {}
    dfs(0)
    print(f'#{t+1} {answer}')
