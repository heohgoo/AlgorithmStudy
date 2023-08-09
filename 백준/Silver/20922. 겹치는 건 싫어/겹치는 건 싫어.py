#투 포인터, 이진탐색
from collections import defaultdict

def solve(n, k, a):
    global answer

    counter = defaultdict(int)
    start, end = 0, 0

    while end < n:
        if counter[a[end]] >= k:
            counter[a[start]] -= 1
            start += 1
        else:
            counter[a[end]] += 1
            end += 1
            answer = max(answer, end-start)



n, k = map(int, input().split())
a = list(map(int, input().split()))
answer = 0

solve(n, k, a)
print(answer)
