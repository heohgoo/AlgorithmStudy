#후위 표기식, 스택
from collections import deque
from string import ascii_uppercase

n = int(input())
exp = list(input())
n_list = deque()
stack = []
operator = ['*', '+', '-', '/']
operand = list(ascii_uppercase)[:n]
dict = {}

for _ in range(n):
    n_list.append(int(input()))

for i in range(n):
    dict[operand[i]] = n_list[i]

for i in range(len(exp)):
    if exp[i] not in operator:
        exp[i] = dict[exp[i]]


def calculate(a, b, e):
    if e == '*':
        return a*b
    elif e == '/':
        return a/b
    elif e == '+':
        return a+b
    else:
        return a-b
    
for i in range(len(exp)):
    if exp[i] not in operator:
        stack.append(exp[i])
    else:
        operand1 = stack.pop()
        operand2 = stack.pop()
        stack.append(calculate(operand2, operand1, exp[i]))

print(format(stack[-1], ".2f"))      