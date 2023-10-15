#스택
from collections import deque


n = int(input())
arr = list(map(int, input().split()))

right_big = [-1]*n
stack = deque()

for i in range(n):
    while stack and stack[-1][1] < arr[i]:
        idx, num = stack.pop()
        right_big[idx] = arr[i]
    stack.append((i, arr[i]))

print(*right_big)