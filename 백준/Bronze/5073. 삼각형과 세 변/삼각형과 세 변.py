import sys


if __name__ == '__main__':

    while True:
        x,y,z = map(int, sys.stdin.readline().split())

        if x == 0 and y == 0 and z == 0:
            break

        if max(x, y, z) < (x+y+z) - max(x, y, z):
            if x == y == z:
                print("Equilateral")
            elif x==y or x==z or y==z:
                print("Isosceles")
            else:
                print("Scalene")

        else:
            print("Invalid")
