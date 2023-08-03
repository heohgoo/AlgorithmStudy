n = int(input())
pillar = []
down = False

for _ in range(n):
    x, y = map(int, input().split())
    pillar.append((x,y))

pillar.sort(key=lambda x:x[0])
k = [0]*(pillar[-1][0]+1)


for x, y in pillar:
    k[x] = y

k = k[pillar[0][0]:]

max_p = 0
idx = 0
for i in range(len(k)):
    if max_p < k[i]:
        idx = i
        max_p = k[i]

max_l = 0

#왼쪽
for i in range(idx):
    max_l = max(max_l, k[i])
    k[i] = max_l

max_r = 0

#오른쪽
for i in range(len(k)-1, idx, -1):
    max_r = max(max_r, k[i])
    k[i] = max_r


answer = sum(k)
print(answer)
