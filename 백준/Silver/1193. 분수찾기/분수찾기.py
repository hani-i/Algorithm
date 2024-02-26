import sys

if __name__ == '__main__':
    X = int(sys.stdin.readline().rstrip('/n'))
    FIRST = 1 #첫번째
    LINE = 1

    while FIRST <= X:
        FIRST += LINE
        LINE += 1

    LINE-=1
    FIRST = FIRST - LINE
    idx = X - FIRST +1 #몇번째인지

    #짝수
    if LINE%2 ==0:
        print(f'{idx}/{LINE-idx+1}')

    else:
        print(f'{LINE-idx+1}/{idx}')



