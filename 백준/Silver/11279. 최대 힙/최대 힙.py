#최대 힙
import heapq

n = int(input())
heap = []
ans = []

for _ in range(n):
    num = int(input())
    if num == 0:
        # -1 곱
        if heap:
            tmp = heapq.heappop(heap)
            ans.append(-tmp)
        else:
            ans.append(0)
    
    else:
        heapq.heappush(heap, -1*num)

for a in ans:
    print(a)
