#해시
n = int(input())
cards = list(map(int, input().split()))
card_dic = {}

for card in cards:
    if card not in card_dic:
        card_dic[card] = 1
    else:
        card_dic[card] += 1

m = int(input())
have_cards = list(map(int, input().split()))
ans = []

for card in have_cards:
    if card not in card_dic:
        ans.append(0)
    else:
        ans.append(card_dic[card])

print(*ans)