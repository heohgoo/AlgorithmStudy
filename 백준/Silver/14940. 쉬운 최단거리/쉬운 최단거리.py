#bfs
import sys
from collections import deque

dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

n, m = map(int, input().split())
grid = []
gx, gy = 0, 0
answer = [[-1]*m for _ in range(n)]

for i in range(n):
    n_list = list(map(int, sys.stdin.readline().split()))
    if 2 in n_list:
        gx = i
        gy = n_list.index(2)

    grid.append(n_list)


def in_range(x, y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def bfs(x, y):
    q = deque()
    q.append((x, y))
    answer[x][y] += 1

    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx+dx, cy+dy

            if not in_range(nx, ny):
                continue

            if answer[nx][ny] == -1 and grid[nx][ny] == 1:
                answer[nx][ny] = answer[cx][cy] + 1
                q.append((nx, ny))


bfs(gx, gy)

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0 and answer[i][j] == -1:
            answer[i][j] = 0

for a in answer:
    print(*a)

