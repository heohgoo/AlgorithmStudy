#에라토스테네스의 채
m, n = map(int, input().split())
num_list = [False, False] + [True]*(n-1)

def make_prime_list():
    for i in range(2, n+1):
        if num_list[i]:
            for j in range(2*i, n+1, i):
                num_list[j] = False

make_prime_list()

for i in range(m, n+1):
    if num_list[i]:
        print(i)