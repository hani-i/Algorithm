receipt = int(input())
type = int(input())
total = 0

for _ in range(type):
    x,y = map(int, input().split())
    total+=x*y

if receipt==total:
    print("Yes")
else : print("No")
