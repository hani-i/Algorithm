import sys

if __name__ == '__main__':
    M = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    list = [] #소수 저장

    for i in range(M,N+1):
        if i == 1:
            continue

        for j in range(2,i):
            if i%j == 0:
                break
        else:
            list.append(i)

    #소수가 없으면 -1 출력
    if len(list) == 0:
        print(-1)

    else:
        print(sum(list))
        print(min(list))