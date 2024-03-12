import sys

def check(n, x, y):
    total = 5000
    for i in range(1, int((n/x)+1)):
        if (n - (x*i))%y == 0:
            tmp = i + (n-(x*i))//y
            if tmp < total:
                total = tmp
    return total

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    value = []

    value.append(check(N,3,5))
    value.append(check(N,5, 3))
    
    if value.count(5000) == 2:
        print(-1)
    else:
        print(min(value))




