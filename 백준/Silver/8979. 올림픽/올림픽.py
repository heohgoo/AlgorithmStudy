n, k = map(int, input().split())
info = []
price_list = []

for i in range(n):
    info.append(list(map(int, input().split())))

info.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)

price = 1
tmp = info[0][1:]
price_list.append(price)

for i in range(1, n):
    if tmp != info[i][1:]:
        price = i+1
    tmp = info[i][1:]
    price_list.append(price)

for i in range(n):
    if info[i][0] == k:
        print(price_list[i])
        break