for f in range(10):
    count = int(input()) 
    inputArr =  list(map(int, input().split()))
    aptNum = 0
    for i in range(2,count-2):
        maxValue = max(inputArr[i-2],inputArr[i-1],inputArr[i+1],inputArr[i+2])
        if maxValue < inputArr[i]:
            aptNum += inputArr[i] - maxValue
    print(f'#{f+1} {aptNum}')