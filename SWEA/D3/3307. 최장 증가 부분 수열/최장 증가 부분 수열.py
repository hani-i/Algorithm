T = int(input())

for t in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    value = [1]*n

    for i in range(n):
        mymax = 0
        for j in range(i):
            if arr[j]<arr[i]:
                if mymax<value[j]:
                    mymax = value[j]

        value[i] = mymax+1

        #print(arr)
        #print(value)
    print(f'#{t+1} {max(value)}')
