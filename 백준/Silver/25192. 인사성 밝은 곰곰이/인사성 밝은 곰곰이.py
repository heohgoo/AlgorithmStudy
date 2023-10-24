import sys

n = int(input())
enter = set([])
ans = 0

for i in range(n):
    next_command = input()
    if next_command == 'ENTER':
        ans += len(enter)
        enter = set([])
    else:
        enter.add(next_command)

    if i == n-1:
        ans += len(enter)

print(ans)