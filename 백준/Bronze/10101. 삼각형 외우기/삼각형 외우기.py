import sys


if __name__ == '__main__':

    x = int(sys.stdin.readline())
    y = int(sys.stdin.readline())
    z = int(sys.stdin.readline())

    if x+y+z == 180:
        if x == y == z:
            print("Equilateral")
        elif x == y or x == z or y ==z :
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Error")
