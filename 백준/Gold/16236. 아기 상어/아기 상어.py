#구현
from collections import deque

dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]
#위, 왼, 오, 아래

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
x, y, baby_shark = 0, 0, 2
ans = 0
eat = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            x, y = i, j
            grid[i][j] = 0


def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


def find_fish(x, y):
    visited = [[False]*n for _ in range(n)]
    distance = [[0]*n for _ in range(n)]
    can_eat_list = []

    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx+dx, cy+dy
            
            if in_range(nx, ny):
                if visited[nx][ny]:
                    continue

                if grid[nx][ny] <= baby_shark:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[cx][cy]+1
                    q.append((nx, ny))

                    if 0 < grid[nx][ny] < baby_shark:
                        can_eat_list.append((nx, ny, distance[nx][ny]))
    
    #거리가 짧은 순, 위쪽, 왼쪽
    can_eat_list.sort(key=lambda x:(x[2], x[0], x[1]))
    return can_eat_list


if __name__ == '__main__':

    while True:
        fishlist = find_fish(x, y)

        if len(fishlist) == 0:
            print(ans)
            break
        
        #상어 이동
        x, y, time = fishlist[0]

        eat += 1
        if baby_shark == eat:
            baby_shark += 1
            eat = 0
        
        grid[x][y] = 0
        ans += time