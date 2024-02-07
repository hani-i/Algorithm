import sys

for i in range(1,int(sys.stdin.readline())+1):
    x,y=map(int,sys.stdin.readline().split())
    print(f'Case #{i}: {x+y}')