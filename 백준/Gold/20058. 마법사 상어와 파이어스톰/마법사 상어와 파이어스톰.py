#구현, bfs
import copy
from collections import deque

def rotate(level):
    for i in range(0, 2**n-2**level+1, 2**level):
        for j in range(0, 2**n-2**level+1, 2**level):
            part = []

            for row in range(i, i+2**level):
                part.append(grid[row][j:j+2**level])

            for k in range(2**level):
                for m in range(2**level):
                    grid[i+k][j+m] = part[2**level-m-1][k]


def ice_melt(arr):
    for i in range(2**n):
        for j in range(2**n):
            cnt = 0

            for dx, dy in zip(dxs, dys):
                nx, ny = i+dx, j+dy
                if not in_range(nx, ny):
                    continue

                if grid[nx][ny] > 0:
                    cnt += 1
            
            if cnt < 3 and grid[i][j] > 0:
                arr[i][j] -= 1
    
    return arr


def in_range(x, y):
    if 0 <= x < 2**n and 0 <= y < 2**n:
        return True
    return False


def find_lump(x, y):
    visited = [[False]*(2**n) for _ in range(2**n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 1

    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx+dx, cy+dy
            if not in_range(nx, ny):
                continue

            if visited[nx][ny]:
                continue

            if grid[nx][ny] > 0:
                q.append((nx, ny))
                cnt += 1
                visited[nx][ny] = True
    
    return cnt
        


dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

n, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2**n)]
magic = list(map(int, input().split()))
ans_sum = 0
ans_cnt = 0

for i in range(q):
    rotate(magic[i])
    tmp = copy.deepcopy(grid)
    grid = ice_melt(tmp)

for row in grid:
    ans_sum += sum(row)

for i in range(2**n):
    for j in range(2**n):
        if grid[i][j] > 0:
            ans_cnt = max(ans_cnt, find_lump(i, j))


print(ans_sum)
print(ans_cnt)