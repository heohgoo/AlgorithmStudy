#스택
n = int(input())
stack = []
op = []
idx = 1
flag = True

for _ in range(n):
    num = int(input())
    
    while idx <= num:
        stack.append(idx)
        op.append('+')
        idx += 1
    
    if stack[-1] == num:
        stack.pop()
        op.append('-')
        continue
    
    else:
       print("NO")
       flag = False
       break

if flag:
    for o in op:
        print(o)