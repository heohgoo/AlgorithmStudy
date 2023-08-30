#bfs
from collections import deque

dxs = [-1, -1, -1, 0, 0, 1, 1, 1]
dys = [-1, 0, 1, -1, 1, -1, 0, 1]

n, m = map(int, input().split())
grid = []
answer = 0
visited = [[0]*m for _ in range(n)]

for _ in range(n):
    grid.append(list(map(int, input().split())))


def in_range(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if not in_range(nx, ny) or (nx, ny) == (x, y):
                continue
            
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx, ny))

            if grid[nx][ny] == 1:
                return visited[nx][ny]
    
    

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            visited = [[0]*m for _ in range(n)]
            answer = max(answer, bfs(i, j))

print(answer)