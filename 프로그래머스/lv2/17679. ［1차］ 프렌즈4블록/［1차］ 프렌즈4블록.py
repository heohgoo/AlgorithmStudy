def find4block(x, y, board):
    cur = board[x][y]
    
    for i in range(2):
        for j in range(2):
            if board[x+i][y+j] != cur:
                return False
    
    return True
    
    
def move(m, n, board):
    
    for i in range(n):       
        flag = False
        tmp = []
        for j in range(m-1, -1, -1):
            if not flag and board[j][i] == 0:
                tx, ty = j, i
                flag = True
                
            if flag and board[j][i] != 0: 
                tmp.append((j, i))
        
            
        for k in range(len(tmp)):
            m_tmp = board[tmp[k][0]][tmp[k][1]]
            board[tx-k][ty] = m_tmp
            board[tmp[k][0]][tmp[k][1]] = 0
    
    return board
    
    
def solution(m, n, board):
    answer = 0
    real = []
    
    for b in board:
        b = list(b)
        real.append(b)
              
    while True:
        remove_list = []

        for i in range(m-1):
            for j in range(n-1):
                if find4block(i, j, real) and real[i][j] != 0: 

                    for k in range(2):
                        for l in range(2):
                            if (i+k, j+l) not in remove_list:
                                remove_list.append((i+k, j+l))
                                answer += 1
        
        if len(remove_list) == 0:
            break
        
        for x, y in remove_list:
            real[x][y] = 0

        real = move(m, n, real)
                

            
    return answer