#bfs
from collections import deque

def move(x, y):
    if visited[x][y] == 0:
        visited[x][y] = 1
        q.append((x, y))

def bfs():
    while q:
        x, y = q.popleft()
        z = c - ( x + y )

        if x == 0:
            result.append(z)
        
        #x에서 빼고, y로
        w = min(x, b-y)
        move(x-w, y+w)
        #x에서 빼고, z로(y는 변화x)
        w = min(x, c-z)
        move(x-w, y)
        #y에서 빼고, z로(x는 변화x)
        w = min(y, c-z)
        move(x, y-w)
        #y에서 빼고, x로
        w = min(y, a-x)
        move(x+w, y-w)
        #z에서 빼고, x로(y는 변화x)
        w = min(z, a-x)
        move(x+w, y)
        #z에서 빼고, y로(x는 변화x)
        w = min(z, b-y)
        move(x, y+w)



q = deque()
result = []
a, b, c = map(int, input().split())
visited = [[0]*(b+1) for _ in range(a+1)]
visited[0][0] = 1
q.append((0, 0))
bfs()
result.sort()
for num in result:
    print(num, end=' ')


