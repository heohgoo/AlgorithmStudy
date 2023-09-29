#bfs
from collections import deque

dxs = [2, 2, -2, -2, 1, 1, -1, -1]
dys = [1, -1, 1, -1, 2, -2, 2, -2]

def in_range(x, y, n):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


def bfs(grid, start, end):
    x, y = start
    ex, ey = end
    q = deque()
    q.append((x, y))
    grid[x][y] = 0

    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy

            if in_range(nx, ny, len(grid)) and grid[nx][ny] == -1:
                q.append((nx, ny))
                grid[nx][ny] = grid[cx][cy] + 1
                if nx == ex and ny == ey:
                    return grid[nx][ny]  
    return 0  


t = int(input())

for _ in range(t):
    n = int(input())
    cx, cy = map(int, input().split())
    wx, wy = map(int, input().split())
    start = (cx, cy)
    end = (wx, wy)

    grid = [[-1]*n for _ in range(n)]

    print(bfs(grid, start, end))
