#set
n, m = map(int, input().split())
hear = set()
see = set()
answer = []

for _ in range(n):
    hear.add(input())

for _ in range(m):
    see.add(input())

answer = sorted(list(hear&see))

print(len(answer))
for a in answer:
    print(a)