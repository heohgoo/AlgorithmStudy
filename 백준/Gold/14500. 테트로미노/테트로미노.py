#구현, dfs
def dfs(x, y, depth, total):
    global result
    #거르는 경우
    if result >= total + maxv*(3-depth):
        return
    if depth == 3:
        result = max(result, total)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                #'ㅗ'자 모양처럼 다시 돌아가서 움직여야 하는 경우
                if depth == 1:
                    visited[nx][ny] = 1
                    dfs(x, y, depth+1, total+board[nx][ny])
                    visited[nx][ny] = 0
                visited[nx][ny] = 1
                dfs(nx, ny, depth+1, total+board[nx][ny])
                visited[nx][ny] = 0


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
board = []
visited = [[0]*m for _ in range(n)]
result = 0
for _ in range(n):
    board.append(list(map(int, input().split())))
maxv = max(map(max, board))
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 0, board[i][j])
        visited[i][j] = 0

print(result)