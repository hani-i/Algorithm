x,y = map(int, input().split())

if(x*60+y<45):
    z = 45-y
    print (f'23 {60-z}')

else:
    z = (x*60+y)-45
    print(f'{z//60} {z%60}')