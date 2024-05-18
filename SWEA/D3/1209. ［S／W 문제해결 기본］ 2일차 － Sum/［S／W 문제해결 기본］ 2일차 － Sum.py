
for _ in range(10):
    tc = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    sum1=[] #행
    #sum2=[] #열
    #sum3=[] #대각선

    tmp3 = 0  # 오른쪽대각선 (같은)
    tmp4 = 0  # 왼쪽대각선

    for i in range(100):
        tmp1=0#행
        tmp2=0#열
        for j in range(100):
            tmp1 += graph[i][j]
            tmp2 += graph[j][i]
            if i == j:
                tmp3+=graph[i][j]
            if i+j == 99:
                tmp4 += graph[i][j]
        sum1.append(tmp1)
        sum1.append(tmp2)
    sum1.append(tmp3)
    sum1.append(tmp4)

    print(f'#{tc} {max(sum1)}')

