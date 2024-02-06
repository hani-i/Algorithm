x,y = map(int, input().split())

if 45<=y:
    print(f'{x} {y-45}')

else:
    if x==0: x=23
    else: x-=1
    print(f'{x} {y+15}')