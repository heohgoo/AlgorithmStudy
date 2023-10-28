#Tree, bfs
import sys
from collections import deque

def bfs():
    while q:
        now = q.popleft()
        for i in graph[now]:
            if nodes[i] == 0:
                nodes[i] = now
                q.append(i)

n = int(input())
graph = [[] for i in range(n+1)]

for _ in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque()
q.append(1)

nodes = [0]*(n+1)

bfs()

for i in nodes[2:]:
    print(i)