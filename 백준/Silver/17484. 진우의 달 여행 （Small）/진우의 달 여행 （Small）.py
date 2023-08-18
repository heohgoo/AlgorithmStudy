#dfs
import sys

dxs = [1, 1, 1]
dys = [-1, 0, 1]

n, m = map(int, input().split())
grid = []
answer = float('inf')

for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))

def in_range(x, y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def travel(x, y, s, before):
    global answer

    if x == n-1:
        answer = min(answer, s)
        return
    
    for i in range(3):
        if i == before:
            continue
        if not in_range(x+dxs[i], y+dys[i]):
            continue

        travel(x+dxs[i], y+dys[i], s+grid[x+dxs[i]][y+dys[i]], i)

for i in range(m):
    travel(0, i, grid[0][i], -1)

print(answer)
