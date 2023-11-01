#stack
from collections import deque

string = input()
exp = input()
stack = []

for i in range(len(string)):
    stack.append(string[i])
    if ''.join(stack[-len(exp):]) == exp:
        for _ in range(len(exp)):
            stack.pop()


if stack:
    print(''.join(stack))
else:
    print('FRULA')