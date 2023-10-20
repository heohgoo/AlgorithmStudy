#에라토스테네스의 채
import sys

MAX = 1000000
prime_list = [False, False] + [True]*(MAX-1)

m = int(MAX**0.5)
for i in range(2, m+1):
    if prime_list[i]:
        for j in range(2*i, MAX+1, i):
            prime_list[j] = False


while True:
    n = int(sys.stdin.readline())
    flag = False
    if n == 0:
        break
    for i in range(3, n, 2):
        if prime_list[i] and prime_list[n-i]:
            flag = True
            print(n, end='')
            print(' = ', end='')
            print(i, end='')
            print(' + ', end='')
            print(n-i)
            break
    
    if not flag:
        print("Goldbach's conjecture is wrong.")