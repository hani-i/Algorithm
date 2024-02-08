import sys

N,X = map(int, sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split(" ",N)))

for a in arr:
    if a<X:
        print(a,end=" ")