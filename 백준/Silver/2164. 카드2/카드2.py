from collections import deque

n = int(input())
cards = deque([i for i in range(1, n+1)])

def solve(cards):
    if len(cards) == 1:
        return cards
    
    while True:
        cards.popleft()
        if len(cards) == 1:
            break
        tmp = cards.popleft()
        cards.append(tmp)
    
    return cards

print(*solve(cards))
