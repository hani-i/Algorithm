T = int(input())

for t in range(T):
    myList = list(map(int, input().split()))
    val = (sum(myList) - max(myList) - min(myList))/8
    print(f'#{t+1} {int(round(val,0))}')
    