v, e = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a][b] = c
    
    
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[k][j]+graph[i][k], graph[i][j])
            

ans = INF
for i in range(1, v+1):
    ans = min(ans, graph[i][i])
    
if ans == INF:
    print(-1)
else:
    print(ans)