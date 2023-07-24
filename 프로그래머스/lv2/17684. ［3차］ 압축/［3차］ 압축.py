from string import ascii_uppercase

def solution(msg):
    answer = []
    d = list(ascii_uppercase)
    idx = 0
    w = ''
    next_idx = 1
    
    while True:
        if idx == len(msg):
            break
                  
        w += msg[idx]
    
                
        if w in d:
            if idx == len(msg)-1:
                answer.append(d.index(w)+1)
            idx += 1
            continue
        else:
            d.append(w)
            answer.append(d.index(w[:-1])+1)
            w = '' 
            
    return answer