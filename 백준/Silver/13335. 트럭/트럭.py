#구현
from collections import deque

n, w, l = map(int, input().split()) #트럭 수, 다리 길이, 최대 하중
trucks = list(map(int, input().split()))
bridge = deque([0]*w)
end = []
t = 0

while True:
    if sum(bridge) == 0 and not trucks:
        break

    t += 1
    if bridge[0] != 0:
        end.append(bridge[0])
        bridge[0] = 0

    bridge.rotate(-1)
    if trucks and sum(bridge) + trucks[0] <= l:
        bridge[-1] = trucks.pop(0)

print(t)