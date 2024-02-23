import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip('/n'))
    coin = [25, 10, 5, 1]

    for i in range(T):
        C = int(sys.stdin.readline().rstrip('/n'))

        for j in range(len(coin)):
            print(C//coin[j], end=" ")
            C = C%coin[j]
        print()






