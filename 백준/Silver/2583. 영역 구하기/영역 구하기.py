#bfs
from collections import deque

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

m, n, k = map(int, input().split())
grid = [[False]*m for _ in range(n)]
answer = []

for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    rx -= 1
    ry -= 1
    for i in range(lx, rx+1):
        for j in range(ly, ry+1):
            grid[i][j] = True

def in_range(x, y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def bfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))
    grid[x][y] = True

    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx+dx, cy+dy
            if in_range(nx, ny) and not grid[nx][ny]:
                grid[nx][ny] = True
                cnt += 1
                q.append((nx, ny)) 
    return cnt


for i in range(n):
    for j in range(m):
        if not grid[i][j]:
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
print(*answer)
