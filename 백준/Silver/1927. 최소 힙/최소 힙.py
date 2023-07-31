#최소 힙
import sys
from heapq import heappop, heappush

n = int(input())
heap = []

for _ in range(n):
    m = int(sys.stdin.readline())
    
    if m == 0:
        if heap:
            tmp = heappop(heap)
            print(tmp)
        else:
            print(0)

    else:
        heappush(heap, m)