x = int(input())


for i in range(1,x+1):
    if i<10:
        if i%3 == 0:
            print("-", end= " ")
        else :
            print(i, end=" ")
    elif 10<=i and i<=99:
        count = 0
        a = i //10
        b = i%10
        if a==3 or a == 6 or a==9:
            count += 1
        if b==3 or b == 6 or b==9:
            count += 1
        if count == 2:
            print("--", end= " ")
        elif count == 1:
            print("-", end= " ")
        else : 
            print(i, end=" ")
    elif 100<=i and i<=999:
        count = 0
        a = i //100
        b =(i%100)//10
        c =(i%100)%10
        if a==3 or a == 6 or a==9:
            count += 1
        if b==3 or b == 6 or b==9:
            count += 1
        if c==3 or c == 6 or c==9:
            count += 1
        if count == 3:
            print("---", end= " ")
        elif count == 2:
            print("--", end= " ")
        elif count == 1:
            print("-", end= " ")
        else : 
            print(i, end=" ")
    else:
        print("1000")