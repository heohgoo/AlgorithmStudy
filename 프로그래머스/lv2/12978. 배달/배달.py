#플로이드 와샬
INF = float("inf")

def solution(N, road, K):
    answer = 0
    graph = [[INF]*(N+1) for _ in range(N+1)]
    
    for i in range(len(graph)):
        graph[i][i] = 0
    
    for r in road:
        graph[r[0]][r[1]] = min(graph[r[0]][r[1]], r[2])
        graph[r[1]][r[0]] = min(graph[r[1]][r[0]], r[2])
        
    for x in range(1, N+1):
        for a in range(1, N+1):
            for b in range(1, N+1):
                graph[a][b] = min(graph[a][x] + graph[x][b], graph[a][b])
                
    distance_list = graph[1][1:]
    
    for d in distance_list:
        if d <= K:
            answer += 1
        
    
    return answer