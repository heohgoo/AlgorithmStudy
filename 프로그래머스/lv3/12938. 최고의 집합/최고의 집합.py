def solution(n, s):
    answer = []
    if s < n:
        return [-1]
    
    c, r = divmod(s, n)
    
    answer = [c]*n
        
    while r:
        for i in range(n-1, -1, -1):
            answer[i] += 1
            r -= 1
            
            if r == 0:
                break
            
    
    return answer