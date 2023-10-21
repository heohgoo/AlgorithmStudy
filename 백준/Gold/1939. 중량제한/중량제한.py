#bfs, 이분탐색
from collections import deque

def bfs(weight):
    q = deque()
    q.append(first)
    visited = [False]*(n+1)
    visited[first] = True

    while q:
        x = q.popleft()

        for y, c in graph[x]:
            if not visited[y] and c >= weight:
                visited[y] = True
                q.append(y)
    
    if visited[second]:
        return True
    else:
        return False
    
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
first, second = map(int, input().split())



start, end = 1, 1000000000
ans = 0

while start <= end:
    mid = (start + end) // 2

    if bfs(mid): #해당 무게로 bfs를 돌려 운반할 수 있다면
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)