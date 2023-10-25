#bfs, 구현
import sys
from collections import deque

dxs = [0, 0, 1, -1]
dys = [-1, 1, 0, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def ripens():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and grid[nx][ny] == 0:
                grid[nx][ny] = grid[x][y] + 1
                q.append((nx, ny))
    
def isComplete():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                return False
    return True


m, n = map(int, input().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            q.append((i, j))

ripens()

if not isComplete():
    print(-1)

else:
    t = 0
    for row in grid:
        t = max(t, max(row))
    
    print(t-1)