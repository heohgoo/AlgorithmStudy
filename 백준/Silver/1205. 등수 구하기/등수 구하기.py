#EOF 에러 
n, score, p = map(int, input().split())

if n > 0:
    rank = list(map(int, input().split()))
else:
    rank = []
price = 0

rank.append(score)
rank.sort(reverse = True)
rank_list = [i for i in range(1, len(rank)+1)]


for i in range(1, len(rank_list)):
    if rank[i] == rank[i-1]:
        rank_list[i] = rank_list[i-1]


for i in range(len(rank_list)-1, -1, -1):
    if rank[i] == score:
        if i+1 > p:
            price = -1
        else:
            price = rank_list[i]
        break

print(price)
