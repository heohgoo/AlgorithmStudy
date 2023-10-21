#우선순위 큐, 힙큐
import heapq

n = int(input())
class_list = []

for _ in range(n):
    class_list.append(tuple(map(int, input().split())))

class_list.sort(key=lambda x:x[0])
q = [class_list[0][1]]

for i in range(1, n):
    if q[0] > class_list[i][0]: #강의실을 쓰고 있으므로 하나 추가
        heapq.heappush(q, class_list[i][1])
    else: #다 쓴 강의실 이어 사용
        heapq.heappop(q)
        heapq.heappush(q, class_list[i][1])

print(len(q))