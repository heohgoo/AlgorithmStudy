#Greedy
t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 1
    info = []
    for _ in range(n):
        info.append(list(map(int, input().split())))
    
    info.sort(key = lambda x:x[0]) #서류 심사 순으로 정렬(높은 등수부터)

    tmp = info[0][1]

    for i in range(1, n):
        if info[i][1] < tmp:
            tmp = info[i][1]
            cnt += 1
    
    print(cnt)
