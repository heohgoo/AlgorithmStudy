#Greedy
n = int(input())
l = list(map(int, input().split()))
answer = [0]*n

for i in range(1, n+1):
    tmp = l[i-1]
    cnt = 0
    for j in range(n):
        if cnt == tmp and answer[j] == 0:
            answer[j] = i
            break
        elif answer[j] == 0:
            cnt += 1

print(*answer)