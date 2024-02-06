H, M = map(int, input().split())
time = int(input())

H+=time//60
M+=time%60

if 60<=M:
    M-=60
    H+=1

if 24<=H:
    H-=24

print(f'{H} {M}')