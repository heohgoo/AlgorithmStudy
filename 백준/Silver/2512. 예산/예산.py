#이진탐색
import sys
input = sys.stdin.readline

n = int(input())
budget = list(map(int, input().split()))
m = int(input())
start, end = 0, max(budget)

if sum(budget) <= m:
    print(end)

else:
    while start <= end:
        total = 0
        mid = (start + end) // 2

        for b in budget:
            total += min(b, mid)
        
        if total > m:
            end = mid - 1

        else:
            start = mid + 1
    
    print(end)