x = int(input())
myLength = 2

for r in range(x):
    mystr = input()
    #print(myLength)
    for k in range(10):
        #print(k, "테스트 k")
        if mystr[0: myLength] != mystr[myLength: 2 * myLength]:
            myLength += 1
            #print(f'test1 {mystr[0: myLength]}, test2{mystr[myLength: 2 * myLength]}')
            #print("길이", myLength)
        elif mystr[30 - 30 % myLength - myLength: 30 - 30 % myLength] != mystr[0: myLength]:
            myLength += 1
            #print("두번째 else문")
        else:
            print(f'#{r + 1} {myLength}')
            myLength = 2
            break
