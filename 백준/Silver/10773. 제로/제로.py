#스택
k = int(input())
stack = []

for _ in range(k):
    n = int(input())

    if n == 0:
        stack.pop()
    else:
        stack.append(n)

if len(stack) == 0:
    print(0)
else:
    print(sum(stack))