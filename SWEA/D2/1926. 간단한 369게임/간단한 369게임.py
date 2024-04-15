x = int(input())


for i in range(1,x+1):
    stri = str(i)
    count = stri.count("3")+stri.count("6")+stri.count("9")
    
    if count == 3:
        print("---", end=" ")
    elif count == 2:
        print("--", end=" ")
    elif count == 1:
        print("-", end=" ")
    else :
        print(stri, end=" ")