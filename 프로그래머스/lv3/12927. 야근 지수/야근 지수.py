#힙
#가장 큰 수를 하나씩 줄여가면서 제곱하는 것이 최소값이 된다.
from heapq import heapify, heappop, heappush

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    w_list = [(-1)*work for work in works]
    heapify(w_list)
    
    while n:
        min_value = heappop(w_list)
        heappush(w_list, min_value+1)
        n -= 1
        
    return sum([w**2 for w in w_list])