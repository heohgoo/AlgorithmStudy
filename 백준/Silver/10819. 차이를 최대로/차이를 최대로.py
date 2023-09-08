#순열
from itertools import permutations

n = int(input())
num = list(map(int, input().split()))
answer = 0

per = list(permutations(num, n))
for p in per:
    tmp = 0
    for i in range(n-1):
        tmp += abs(p[i] - p[i+1])
    answer = max(answer, tmp)

print(answer)