n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
def dfs(start, visited):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            dfs(i, visited)
            
cnt = 0

for i in range(1, n+1):
    if visited[i] == False:
        cnt += 1
        dfs(i, visited)
    
print(cnt)