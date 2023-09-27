#변 a,b,c
from itertools import combinations

n = int(input())
answer = 0

for a in range(1, n):
    for b in range(a, n):
        c = n - (a + b)
        if c < b:
            break
        if b+a > c:
            answer += 1

print(answer)