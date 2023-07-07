#dp
# def solution(n):
#     num = [0]*(n+1)
    
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             num[i] = num[i//2]
#         else:
#             num[i] = num[i-1]+1
        
#     return num[n] 

def solution(n):
    cnt = 0
    while n > 0:
        if n % 2 == 0:
            n = n//2
        else:
            n -= 1
            cnt += 1
    return cnt