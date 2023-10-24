import sys

n = int(input())
dance = {'ChongChong'}

for _ in range(n):
    first, second = map(str, sys.stdin.readline().split())
    if first in dance or second in dance:
        dance.update({first, second})

print(len(dance))