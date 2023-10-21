#우선순위 큐
import sys
import heapq

n, k = map(int, input().split()) #보석, 가방
jew = []
bag = []
heap = []
ans = 0

for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(jew, [m, v])

for _ in range(k):
    bag.append(int(sys.stdin.readline()))
    
bag.sort()

for i in range(k):
    while jew and bag[i] >= jew[0][0]:
        heapq.heappush(heap, -jew[0][1])
        heapq.heappop(jew)
    
    if heap:
        ans -= heapq.heappop(heap)

print(ans)