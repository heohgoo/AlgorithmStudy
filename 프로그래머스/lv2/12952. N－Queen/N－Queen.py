#N-Queen, 백트래킹    
answer = 0

def solution(n):  
    board = [0]*n
    visited = [False]*n
    
    def dfs(depth):
        global answer
        
        if depth == n:
            answer += 1
            return
        
        for i in range(n):
            if not visited[i]:
                board[depth] = i
            
                if check(depth): #백트래킹
                    visited[i] = True
                    dfs(depth+1)
                    visited[i] = False
    
    def check(num):
        for i in range(num):
            if board[num] == board[i] or abs(board[num] - board[i]) == abs(num - i):
                return False
        return True
    
    dfs(0)
            
    return answer