def solution(park, routes):
    answer = []
    myPark = [[0 for _ in range(len(park[1]))] for _ in range(len(park))]
    start = [0,0]
    tmpH = 0
    
    #park 문자열을 myPark 배열에 삽입
    for p in park:
        print(p)
        for i in range(len(p)):
            myPark[tmpH][i] = p[i]
            if p[i] == "S":
                start[0] = tmpH
                start[1] = i
        tmpH+=1
        
    
    for i in range(len(routes)):
        op, n = routes[i].split()
        n = int(n)
        tmps = start[:]
  
        for j in range(n):
    
            if op=="E":
                tmps[1] = tmps[1] +1
                
            elif op=="W":
                tmps[1] = tmps[1] -1
                
            elif op=="S":
                tmps[0] = tmps[0] +1
                
            elif op=="N":
                tmps[0] = tmps[0] -1      
            
            if tmps[0] >= len(myPark) or tmps[1] >= len(myPark[1]) or tmps[0]<0 or tmps[1]<0:
                tmps = start[:]
                break        
            elif myPark[tmps[0]][tmps[1]] == "X":
                tmps = start[:]
                break
                      
            if j == n-1:
                start = tmps[:]
    return start