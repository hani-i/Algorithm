import sys

c = int(sys.stdin.readline())
arr =list(map(int, sys.stdin.readline().split(" ",c)))
num = int(sys.stdin.readline())

print(arr.count(num))