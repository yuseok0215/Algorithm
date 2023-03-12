import sys
sys.setrecursionlimit(10**6)

T = int(input())

def dfs(x,y):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx < M) and (0 <= ny < M):
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(nx, ny)
                
                
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
        
    
    for x in range(M):
        for y in range(N):
            if graph[x][y] == 1:
                dfs(x,y)
                cnt += 1
                
                
    print(cnt)