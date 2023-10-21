#MST(크루스칼)
def find_parent(parent, x):
    if parent[x] == x:
        return x
    return find_parent(parent, parent[x])

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


v, e = map(int, input().split())
parent = [i for i in range(v+1)]
ans = 0
cnt = 0
info = []

for _ in range(e):
    info.append(tuple(map(int, input().split())))

info.sort(key=lambda x:x[2])

for i in info:
    if find_parent(parent, i[0]) != find_parent(parent, i[1]):
        union_parent(parent, i[0], i[1])
        ans += i[2]
        cnt += 1
    
    if cnt == v-1:
        break

print(ans)
