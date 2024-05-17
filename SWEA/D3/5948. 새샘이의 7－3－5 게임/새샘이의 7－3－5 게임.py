
T = int(input())

for t in range(T):
    myList = list(map(int,input().split()))
    mySet = set()
    for i in range(5):
        for j in range(i+1,6):
            for k in range(j+1,7):
                s = myList[i] + myList[j]+ myList[k]
                mySet.add(s)
    mySet = sorted(mySet)
    S = list(mySet)
    #print(S)
    print(f'#{t+1} {S[len(S)-5]}')