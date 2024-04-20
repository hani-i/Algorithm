
T = int(input())

for t in range(T):
    Line = int(input())
    myList = list(map(int, input().split()))
    value = [0] * 101
    
    myMax = 0
    maxIdx = 0
    #각 점수의 인덱스에 저장함으로써 횟수를 저장
    for i in myList:
        value[i] += 1
        
    for i in range(len(value)):
        if value[i] > myMax:
            maxIdx = i
            myMax = value[i]
    
    #최빈값이 여러개일 경우 인덱스(점수)가 높은 것을 출력
    for i in range(len(value)):
        if value[i] == myMax and maxIdx < i:
            maxIdx = i
            
     
    print(f'#{Line} {maxIdx}')
    
    
    
    