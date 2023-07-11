#하노이의 탑
result = []

def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        result.append([from_pos, to_pos])
        return 
    
    hanoi(n-1, from_pos, aux_pos, to_pos) #원반 n-1개를 aux_pos로 옮김
    result.append([from_pos, to_pos])
    hanoi(n-1, aux_pos, to_pos, from_pos) #원반 n-1개를 to_pos로 옮김
        
def solution(n):
    hanoi(n, 1, 3, 2)
    return result