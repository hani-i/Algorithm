T = int(input())

for t in range(T):
    x = list(input())
    init = "0"*len(x)
    init = list(init)
    count = 0


    for i in range(len(init)):
        if x==init:
            break

        if x[i] != init[i] and init[i] == "0":
            #init[i:] = "1"
            for j in range(i,len(x)):
                init[j] = "1"
            count+=1
        elif x[i]!=init[i] and init[i]=="1":
            #init[i:] = "0"
            for j in range(i,len(x)):
                init[j] = "0"
            count+=1
        else:
            continue
        #print(init)
    print(f'#{t+1} {count}')