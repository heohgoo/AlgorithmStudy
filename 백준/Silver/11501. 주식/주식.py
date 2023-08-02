#그리디
t = int(input())

for _ in range(t):
    days = int(input())
    price = list(map(int, input().split()))
    max_price = 0
    answer = 0

    for i in range(days-1, -1, -1):
        if price[i] > max_price:
            max_price = price[i]
        else:
            answer += max_price - price[i]
    
    print(answer)
