#Greedy
n = int(input())
score = []
count = 0

for _ in range(n):
    score.append(int(input()))

start = score[-1]
for i in range(n-2, -1, -1):
    if start > score[i]:
        start = score[i]
        continue

    tmp = start - 1
    count += score[i] - tmp
    start = tmp

print(count)