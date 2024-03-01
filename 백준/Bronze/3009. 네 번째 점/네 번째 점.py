import sys



if __name__ == '__main__':
    xlist = []
    ylist = []
    x = 0
    y = 0

    for _ in range(3):
        a, b = map(int,sys.stdin.readline().split())
        xlist.append(a)
        ylist.append(b)

    for i in range(3):
        if xlist.count(xlist[i]) == 1:
            x = xlist[i]
            
        if ylist.count(ylist[i]) == 1:
            y = ylist[i]

    print(x,y)


