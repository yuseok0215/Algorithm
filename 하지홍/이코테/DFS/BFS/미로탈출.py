n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split)))
    
    
direction = [[1,0],[-1,0],[0,-1],[0,1]]

from collections import deque


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        
        for move_x, move_y in direction:
            next_x = move_x + x
            next_y = move_y + y
            
            if 0 <= next_x <= n and 0 <= next_y <= m:
                if graph[next_x][next_y] == 1:
                    graph[next_x][next_y] = graph[x][y] + 1
                    queue.append((next_x,next_y))
    return graph[n-1][m-1]

print(bfs(0,0))
    