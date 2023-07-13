from math import factorial, floor

def solution(n, k):
    answer = []
    n_list = [i for i in range(1, n+1)]
    
    if n == 1:
        return [1]
        
    for i in range(n-1, 0, -1):
        n_f = factorial(i)
        c = floor(k/n_f)
        r = k % n_f
        
        if r != 0:
            c += 1
            
        answer.append(n_list[c-1])
        n_list.remove(n_list[c-1])
        
        k = r
        if k == 0:
            n_list.reverse()
            for n in n_list:
                answer.append(n)
            break      
        
    return answer