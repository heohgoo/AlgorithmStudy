from math import ceil

def solution(n, stations, w):
    answer = 0
    idx = 1
    
    
    for s in stations:
        l = s - w if s - w >= 1 else 1
        r = s + w if s + w <= n else n
        
        answer += ceil((l - idx) / (2 * w + 1))
        idx = r + 1
        
    if (n - idx) >= 0:
        answer += ceil((n - idx + 1) / (2 * w + 1))    

    return answer