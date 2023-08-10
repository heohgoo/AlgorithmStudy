n, d = map(int, input().split())
highway = [i for i in range(d+1)]
info = []

for _ in range(n):
    info.append(list(map(int, input().split())))

info.sort(key=lambda x:x[0])

for i in info:
    start, end, length = i
    idx = 0
    if end > d:
        continue

    for i in range(end, len(highway)):
        highway[i] = min(highway[i], highway[start] + length + idx)
        idx += 1


print(highway[-1])