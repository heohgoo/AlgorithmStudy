#greedy
n, k = map(int, input().split())
restaurant = list(input())
ans = 0

for i in range(n):
    if restaurant[i] == 'P':
        # 왼쪽부터 탐색해 나간다.
        for j in range(max(0, (i-k)), min(n, i+k+1)):
            if restaurant[j] == 'H':
                restaurant[j] = 'E'
                ans += 1
                break

print(ans)
