#구현
def in_range(x, y, n):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


def tornado(time, dx, dy, dir):
    global ans, cx, cy

    for _ in range(time):
        cx, cy = cx + dx, cy + dy
        
        if cy < 0:
            break
        
        total = 0
        for x, y, p in dir:
            nx, ny = cx + x, cy + y
            if p == 1: #alpha
                sand = grid[cx][cy] - total
            else:
                sand = int(grid[cx][cy]*p)
                total += sand
            
            if in_range(nx, ny, n):
                grid[nx][ny] += sand
            else:
                ans += sand


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
cx, cy = n//2, n//2

left = [(-1, 1, 0.01), (1, 1, 0.01), (-1, 0, 0.07), (1, 0, 0.07), (2, 0, 0.02), (-2, 0, 0.02)
        , (-1, -1, 0.1), (1, -1, 0.1), (0, -2, 0.05), (0, -1, 1)]
right = [(x, -y, p) for x, y, p in left]
up = [(y, x, p) for x, y, p in left]
down = [(-y, x, p) for x, y, p in left]

ans = 0

for i in range(1, n+1):
    if i % 2 == 1:
        tornado(i, 0, -1, left)
        tornado(i, 1, 0, down)
    else:
        tornado(i, 0, 1, right)
        tornado(i, -1, 0, up)

print(ans)