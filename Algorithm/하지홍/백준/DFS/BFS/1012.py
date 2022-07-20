import sys
T = int(input())
sys.setrecursionlimit(10000)
direction = [[1,0],[-1,0],[0,-1],[0,1]]


def dfs(x,y):
    graph[x][y] = 2
    for next_move_x, next_move_y in direction:
        next_x = x + next_move_x
        next_y = y + next_move_y
        
        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
            continue
        if graph[next_x][next_y] == 1:
            graph[next_x][next_y] = 2
            dfs(next_x, next_y)
            
for i in range(T):
    m, n, k = map(int, input().split())
    
    graph = [[0] * (m) for _ in range(n)]
    cnt = 0
    
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
        
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i,j)
                cnt += 1
                
    print(cnt)       
    
    
    
