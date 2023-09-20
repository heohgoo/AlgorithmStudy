#bfs
import sys
from collections import deque

input = sys.stdin.readline

def bfs(idx, cnt):
    q = deque()
    q.append(idx)
    visited[idx] = True
    
    while q:
        if visited.count(True) == n:
            return cnt
        
        c = q.popleft()

        for node in graph[c]:
            if not visited[node]:
                q.append(node)
                cnt += 1
                visited[node] = True


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    print(bfs(1, 0))
