n1, n2 = map(int, input().split())
left = list(input())
right = list(input())
t = int(input())

bridge = []

for i in range(n1-1, -1, -1):
    bridge.append(left[i])

for i in range(n2):
    bridge.append(right[i]) 


def move():
    idx = []

    for i in range(1, len(bridge)):
        if bridge[i] in right and bridge[i-1] in left:
            idx.append(i)
    
    for i in idx:
        tmp = bridge[i]
        bridge[i] = bridge[i-1]
        bridge[i-1] = tmp

for i in range(t):
    move()

print("".join(bridge))