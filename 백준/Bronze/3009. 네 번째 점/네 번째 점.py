import sys

def check(list):
    if list.count(list[0]) == 1:
        return list[0]
    elif list.count(list[1]) == 1:
        return list[1]
    else:
        return list[2]


if __name__ == '__main__':
    a, d = map(int, sys.stdin.readline().split())
    b, e = map(int, sys.stdin.readline().split())
    c, f = map(int, sys.stdin.readline().split())

    Xlist = [a, b, c]
    Ylist = [d, e, f]

    print(check(Xlist), end=" ")
    print(check(Ylist))


