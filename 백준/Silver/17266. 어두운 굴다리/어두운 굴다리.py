import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
loc = list(map(int, input().split()))

max_height = 0

for i in range(1, m):
    max_height = max(max_height, loc[i] - loc[i-1])

answer = max((max_height+1)//2, loc[0] - 0, n - loc[-1])
print(answer)