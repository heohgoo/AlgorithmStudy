#해시
n = int(input())
info = {}
ans = []

for _ in range(n):
    name, what = map(str, input().split())
    info[name] = what


for name in info:
    if info[name] == 'enter':
        ans.append(name)

ans.sort(reverse=True)

for a in ans:
    print(a)