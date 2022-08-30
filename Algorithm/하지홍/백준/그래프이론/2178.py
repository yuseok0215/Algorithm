from collections import deque

n , m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))
    
direction = [[1,0],[-1,0],[0,-1],[0,1]]

def bfs(x,y):
    queue = deque()
    
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        
        
        for next_move_x, next_move_y in direction:
            next_x = x + next_move_x
            next_y = y + next_move_y
            
            if next_x < 0 or next_y < 0  or next_x >= n or next_y >= m:
                continue
            if graph[next_x][next_y] == 0:
                continue
            
            if graph[next_x][next_y] == 1:
                graph[next_x][next_y] = graph[x][y] + 1
                queue.append((next_x, next_y))
                
    return graph[n-1][m-1]
            
print(bfs(0,0))