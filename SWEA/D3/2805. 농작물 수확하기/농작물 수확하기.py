T = int(input())

for t in range(T):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input()))

    up = n//2
    down = n-up

    x = 0
    y = n//2
    k = 1
    sum = 0

    for _ in range(up+1):
        for j in range(y, y+k):
            sum += arr[x][j]

        if k == n:
            break
        k += 2
        x += 1
        y -= 1

    for _ in range(down-1):
        k -= 2
        x += 1
        y += 1
        for j in range(y, y+k):
            sum += arr[x][j]

    print(f'#{t+1} {sum}')