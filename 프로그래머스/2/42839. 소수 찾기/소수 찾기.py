count = 0
saveArray = []
def isprimeNumber(arr):
    stringNumber = "".join(map(str,arr))
    intNumber = int(stringNumber)
    
    for i in range(2,(int)(intNumber/2)+1):
        if intNumber%i ==0:
            return False
    
    return True

def permutation(arr,visited,result,n):
    global count
    global saveArray
    if len(result)==n:
        stringNumber = "".join(map(str,result))
        intNumber = int(stringNumber)
        if (isprimeNumber(result) and intNumber not in saveArray and intNumber>1):
            print(stringNumber)
            count += 1
            saveArray.append(intNumber)
        return
    
    else:
        for i in range(len(arr)):
            if visited[i] == 0:
                visited[i] = 1
                result.append(arr[i])
                permutation(arr,visited,result,n)
                visited[i] = 0
                result.pop()
                


def solution(numbers):
    arr = list(map(int,numbers))
    result = []
    visited = [0]*len(arr)
    
    for i in range(1,len(numbers)+1):
        permutation(arr, visited, result, i)
    
    
    
    
    # permutation(arr, visited, result, 2)
    return count
    