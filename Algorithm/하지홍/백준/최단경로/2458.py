import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

ans = 0

for _  in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1
    
for i in range(1, n+1):
    temp = 0
    for j in range(1, n+1):
        temp += graph[i][j] + graph[j][i]
        
    if temp == n-1:
        ans += 1
        
print(ans)