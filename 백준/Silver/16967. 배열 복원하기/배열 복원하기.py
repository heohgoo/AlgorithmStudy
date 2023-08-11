h, w, x, y = map(int, input().split())
grid = []
tmp = [[0]*w for _ in range(h)]


for _ in range(h+x):
    grid.append(list(map(int, input().split())))


for i in range(h):
    for j in range(w):
        if x<=i<x+h and y<=j<y+w:
            continue
            # tmp[i][j] = grid[i+x][j+y] - grid[i][j]
        else:
            tmp[i][j] = grid[i][j]


for i in range(h):
    for j in range(w):
        if x<=i<x+h and y<=j<y+w:
            tmp[i][j] = grid[i][j] - tmp[i-x][j-y] 


for t in tmp:
    print(*t)