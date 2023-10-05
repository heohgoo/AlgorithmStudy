#유클리드-호제
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
answer = 0

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

print('1'*gcd(a, b))