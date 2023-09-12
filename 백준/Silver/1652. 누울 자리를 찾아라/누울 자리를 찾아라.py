n = int(input())
grid = list(list(input()) for _ in range(n))
row, column = 0, 0

for i in range(n):
    flag = True
    for j in range(n-1):
        if flag and grid[i][j] == '.' and grid[i][j+1] == '.':
            row += 1
            flag = False
        
        if grid[i][j] == 'X':
            flag = True

for i in range(n):
    flag = True
    for j in range(n-1):
        if flag and grid[j][i] == '.' and grid[j+1][i] == '.':
            column += 1
            flag = False
        
        if grid[j][i] == 'X':
            flag = True

print(row, end = " ")
print(column)