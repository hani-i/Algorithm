import sys

count = int(sys.stdin.readline())
str = sys.stdin.readline().rstrip("\n")
arr = str.split(' ',count-1)

for i in range(0,count):
    arr[i]=int(arr[i])

num = int(sys.stdin.readline())

c = 0
for a in arr:
    if a==num:
        c+=1

print(c)