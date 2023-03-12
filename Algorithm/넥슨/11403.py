from collections import deque

n = int(input())

graph = []

for _ in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

new_graph = [[0]*(n) for _ in range(n)]

def bfs(x):
    queue = deque()
    queue.append(x)
    check = [0 for _ in range(n)]
    
    while queue:
        q = queue.popleft()
        
        for i in range(n):
            if check[i] == 0 and graph[q][i] == 1:
                check[i] = 1
                new_graph[x][i] = 1
                queue.append(i)
                
for i in range(0, n):
    bfs(i)
    
for elem in new_graph:
    print(*elem)