# answer, tmp = 0, 0

# def solution(land):   
#     def dfs(depth, n):
#         global answer, tmp
        
#         if depth == len(land):
#             answer = max(answer, tmp)
#             return
        
#         for i in range(4):
#             if i != n:                                 
#                 tmp += land[depth][i]
#                 dfs(depth+1, i)   
#                 tmp -= land[depth][i]
#     dfs(0, 0)
   
#     return answer

def solution(land):
    
    for i in range(1, len(land)):
        for j in range(4):
            tmp = land[i-1][j]
            land[i-1][j] = -1
            land[i][j] += max(land[i-1][0], land[i-1][1], land[i-1][2], land[i-1][3])
            land[i-1][j] = tmp
    
    
    
    return max(land[-1])
    