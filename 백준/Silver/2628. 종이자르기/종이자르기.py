n, m = map(int, input().split())

row = [0, m]
column = [0, n]

num = int(input())
for _ in range(num):
    r_or_c, line = map(int, input().split())
    if r_or_c == 0:
        row.append(line)
    else:
        column.append(line)

row.sort()
column.sort()

component_row = []
component_column = []

for i in range(len(row)-1):
    component_row.append(row[i+1] - row[i])

for i in range(len(column)-1):
    component_column.append(column[i+1] - column[i])

print(max(component_row)*max(component_column))