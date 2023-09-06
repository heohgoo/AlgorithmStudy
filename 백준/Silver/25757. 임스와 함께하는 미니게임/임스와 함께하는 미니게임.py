n, game = input().split()
n = int(n)
player = []
answer = 0

for _ in range(n):
    player.append(input())

player = set(player)
p_len = len(player)

if game == 'Y':
    answer = p_len
elif game == 'F': 
    answer = p_len//2
else:
    answer = p_len//3

print(answer)
