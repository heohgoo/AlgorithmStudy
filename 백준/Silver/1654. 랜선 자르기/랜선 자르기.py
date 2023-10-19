#이분탐색
k, n = map(int, input().split())
lans = []

for _ in range(k):
    lans.append(int(input()))

start, end = 1, max(lans)

while start <= end: #start가 end와 같으면 출력
    mid = (start + end) // 2
    lines = 0

    for lan in lans:
        lines += lan // mid
    
    if lines >= n:
        start = mid + 1
    
    else:
        end = mid - 1

print(end)