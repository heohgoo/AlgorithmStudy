import sys
input = sys.stdin.readline

n, l = map(int, input().split())
loc = list(map(int, input().split()))
stack = []
answer = 0

loc.sort()

for w in loc:
    left, right = w-0.5, w+0.5
    if stack and right - stack[0] > l:
        stack = [left, right]
        answer += 1
    else:
        stack.extend([left, right])

if stack:
    answer += 1

print(answer)
