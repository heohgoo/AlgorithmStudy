#Greedy
n = int(input())
rope = []
answer = 0

for _ in range(n):
    rope.append(int(input()))

rope.sort()

for i in range(n):
    answer = max(answer, rope[i]*(n-i))

print(answer)