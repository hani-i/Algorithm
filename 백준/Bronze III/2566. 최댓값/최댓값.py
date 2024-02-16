nums = []

for _ in range(9):
    nums.append(list(map(int,input().split())))

x = 0
y = 0
max_num = -1
for i in range(9):
    for j in range(9):
        if nums[i][j] > max_num:
            x = i + 1
            y = j + 1
            max_num= nums[i][j]
print(max_num)
print(x, y)