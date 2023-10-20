#스택
n = int(input())

for _ in range(n):
    stack = []
    ps = list(input())

    for i in range(len(ps)):
        if not stack:
            stack.append(ps[i])
            continue

        if ps[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(ps[i])
        
        else:
            stack.append(ps[i])

    if stack:
        print("NO")
    else:
        print("YES")