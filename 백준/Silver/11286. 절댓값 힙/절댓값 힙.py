#힙
import heapq

n = int(input())
heap = []
ans = []

for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, (abs(num), num)) #튜플 사용 시 앞문자만 가지고 정려한다.
    else:
        if not heap:
            ans.append(0)
        else:
            _, pop_num = heapq.heappop(heap)
            ans.append(pop_num)

for a in ans:
    print(a)