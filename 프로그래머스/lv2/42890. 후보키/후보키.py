#조합
from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    c = []
    
    for i in range(1, col+1):
        c.extend(combinations(range(col), i))
    
    unique = []
    
    for i in c:
        flag = False
        
        tmp = [tuple(item[key] for key in i) for item in relation]
        #모든 경우의 리스트 하나씩
        if len(set(tmp)) == row: #유일성 만족하는가
            flag = True
            
            for u in unique:
                if set(u).issubset(set(i)): #부분집합에 포함되는지 확인, 최소성 만족하는가
                    flag = False
                    break
        if flag:
            unique.append(i)
            
    return len(unique)