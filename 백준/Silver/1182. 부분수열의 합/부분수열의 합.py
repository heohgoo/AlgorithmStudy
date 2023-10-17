#브루트포스(조합)
from itertools import combinations

n, s = map(int, input().split())
num_list = list(map(int, input().split()))
ans = 0

combi = []

for i in range(1, n+1):
    combi.append(list(combinations(num_list, i)))

for tup in combi:
    if tup:
        for i in tup:
            tmp = 0
            tmp = sum(i)
            if tmp == s:
                ans += 1

print(ans)