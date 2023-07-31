import sys

n, m = map(int, input().split())
memo = {}

for _ in range(n):
    word = sys.stdin.readline().strip()
    memo[word] = 1

#m:2*10^5, n:2*10^5, tmp:10
for _ in range(m):
    tmp = sys.stdin.readline().strip()
    tmp = tmp.split(',')
    for t in tmp:
        if t in memo and memo[t] == 1:
            memo[t] = 0
            n -= 1
    print(n)