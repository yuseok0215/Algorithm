n, k = map(int, input().split())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(k):
    a,b = map(int, input().split())
    graph[a][b] = 1
    
    
    
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
                
                
m = int(input())
for _ in range(m):
    x,y = map(int, input().split())
    if graph[x][y]:
        print(-1)
    elif graph[x][y]:
        print(1)
    else:
        print(0)